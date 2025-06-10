import requests
from bs4 import BeautifulSoup
import mysql.connector
import csv
import time
import threading
import keyboard
import sys

# --- Configuration ---
BASE_IP = '139.6.65.27'  # <<<<<< HIER IP EINMAL ÄNDERN

# --- DB configurations ---
DB1_CONFIG = {
    'host': BASE_IP,
    'port': 31006,
    'user': 'wfc',
    'password': 'wfc',
    'database': 'times'
}

DB2_CONFIG = {
    'host': BASE_IP,
    'port': 31007,
    'user': 'wfc',
    'password': 'wfc',
    'database': 'maps'
}

# --- RabbitMQ configurations ---
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'
RABBITMQ_QUEUE = 'maptickets'  # <<< ggf. anpassen
RABBITMQ_API_URL = f'http://{BASE_IP}:31672/api/queues/%2F/{RABBITMQ_QUEUE}'

def is_queue_empty():
    try:
        response = requests.get(RABBITMQ_API_URL, auth=(RABBITMQ_USER, RABBITMQ_PASS))
        if response.ok:
            data = response.json()
            messages = data.get('messages', -1)
            print(f"Queue '{RABBITMQ_QUEUE}' has {messages} messages.")
            return messages == 0
        else:
            print(f"Failed to get queue status: {response.status_code} {response.text}")
            return False
    except Exception as e:
        print(f"Error checking RabbitMQ queue: {e}")
        return False

numberOfWorkers = int(sys.argv[1])

# --- Constants ---
CSV_PATH = 'messreihen.csv'
UUID_COLUMN_NAME = 'uuid'
DB_VALUE_COLUMN_NAME = 'total'
STATUS_POLL_INTERVAL = 5  # seconds between status checks
MAX_WAIT_TIME = 1200      # max seconds to wait per row

# --- Exit flag ---
exit_requested = False
immediate_exit_requested = False

def watch_for_exit():
    global exit_requested
    print("Press 'X' to stop the script gracefully.")
    keyboard.wait('x')
    print("\nExit requested. Finishing current row and saving...")
    exit_requested = True

def watch_for_immediate_exit():
    global immediate_exit_requested
    print("Press 'Q' to stop the script gracefully immediately.")
    keyboard.wait('q')
    print("\nExit requested. saving...")
    immediate_exit_requested = True

# Start key listener in background
threading.Thread(target=watch_for_exit, daemon=True).start()
threading.Thread(target=watch_for_immediate_exit, daemon=True).start()

# --- Step 1: Read and process CSV ---
updated_rows = []
with open(CSV_PATH, mode='r', newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)

    if UUID_COLUMN_NAME not in headers:
        headers.append(UUID_COLUMN_NAME)
    if DB_VALUE_COLUMN_NAME not in headers:
        headers.append(DB_VALUE_COLUMN_NAME)
        
    for row_index, row in enumerate(reader, start=1):
        if exit_requested:
            updated_rows.append(row)
            break

        print("Row: ", row)
        if int(row[2]) == numberOfWorkers and (len(row) < 7 or row[6].strip() == ''):
            payload = {
                'var1': str(row[0]),
                'var2': str(row[1]),
                'var3': "0",
                'var4': str(row[2])
            }
            
            response = requests.post(f"http://{BASE_IP}:31000/setRules", data=payload)
            time.sleep(30)

            # --- Step 2: Send POST request ---
            try:
                response = requests.post(f"http://{BASE_IP}:31001/mapGenerator")
                if response.ok:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    uuid_tag = soup.h1
                    uuid = uuid_tag.text.strip() if uuid_tag else ''
                else:
                    uuid = ''
            except Exception as e:
                print(f"Error during POST for row {row_index}: {e}")
                uuid = ''

            db_value = ''
            if uuid:
                start_time = time.time()
                while True:
                    if immediate_exit_requested:
                        break
                    try:
                        conn2 = mysql.connector.connect(**DB2_CONFIG)
                        cursor2 = conn2.cursor()
                        cursor2.execute("SELECT mapID FROM mapchunks WHERE mapID = %s GROUP BY mapID HAVING SUM(CASE WHEN computed IS NOT TRUE THEN 1 ELSE 0 END) = 0", (uuid,))
                        
                        status_result = cursor2.fetchone()
                        cursor2.close()
                        conn2.close()

                        if status_result:
                            print(f"Computation complete for UUID {uuid}")

                            # --- Warte auf leere RabbitMQ Queue ---
                            print("Waiting for RabbitMQ queue to empty...")
                            while not is_queue_empty():
                                if immediate_exit_requested:
                                    break
                                time.sleep(5)
                            print("RabbitMQ queue is empty. Continuing...")

                            break
                    except mysql.connector.Error as err:
                        print(f"MySQL error (status DB) for UUID {uuid}: {err}")

                    time.sleep(STATUS_POLL_INTERVAL)
                
                time.sleep(STATUS_POLL_INTERVAL*2)                
                try:
                    conn1 = mysql.connector.connect(**DB1_CONFIG)
                    cursor1 = conn1.cursor()
                    cursor1.execute("SELECT totalDuration FROM mapTimes WHERE mapID = %s LIMIT 1", (uuid,))
                    result = cursor1.fetchone()
                    db_value = result[0] if result else ''
                    cursor1.close()
                    conn1.close()
                except mysql.connector.Error as err:
                    print(f"MySQL error (main DB) for UUID {uuid}: {err}")
                    db_value = ''
            
            if immediate_exit_requested:
                updated_rows.append(row)
                break
            
            while len(row) < len(headers):
                row.append('')
            row[headers.index(UUID_COLUMN_NAME)] = uuid
            row[headers.index(DB_VALUE_COLUMN_NAME)] = db_value

        updated_rows.append(row)
        
    for remaining_row in reader:
        updated_rows.append(remaining_row)

# --- Step 6: Write updated CSV ---
with open(CSV_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(updated_rows)

print("CSV fully processed.")
