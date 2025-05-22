import requests
from bs4 import BeautifulSoup
import mysql.connector
import csv
import time

# --- DB configurations ---
DB1_CONFIG = {
    'host': '192.168.178.56',
    'port': 31006,
    'user': 'wfc',
    'password': 'wfc',
    'database': 'times'
}

DB2_CONFIG = {
    'host': '192.168.178.56',
    'port': 31007
    'user': 'wfc',
    'password': 'wfc',
    'database': 'maps'
}

numberOfWorkers = 1

# --- Constants ---
CSV_PATH = 'messreihen.csv'
UUID_COLUMN_NAME = 'uuid'
DB_VALUE_COLUMN_NAME = 'total'
STATUS_POLL_INTERVAL = 5  # seconds between status checks
MAX_WAIT_TIME = 1200        # max seconds to wait per row

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
    
        if (row[2] == numberOfWorkers):
            # Build payload from row (customize)
            payload = {
                'numberOfTiles': row[0],
                'numberOfParts': row[1],
                'numberOfWorkers': row[2],
                'entropyTolerance': 5
            }
            
            response = requests.post("http://192.168.178.56:31000/setRules", data=payload)

            # --- Step 2: Send POST request ---
            try:
                response = requests.post("http://192.168.178.56:31001/mapGenerator")
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
                # --- Step 3: Query main DB for data ---
                try:
                    conn1 = mysql.connector.connect(**DB1_CONFIG)
                    cursor1 = conn1.cursor()
                    cursor1.execute("SELECT totalDuration FROM mapTimes WHERE mapID = %s", (uuid,))
                    result = cursor1.fetchone()
                    db_value = result[0] if result else ''
                    cursor1.close()
                    conn1.close()
                except mysql.connector.Error as err:
                    print(f"MySQL error (main DB) for UUID {uuid}: {err}")
                    db_value = ''

                # --- Step 4: Poll status DB until computation is done ---
                start_time = time.time()
                while True:
                    try:
                        conn2 = mysql.connector.connect(**DB2_CONFIG)
                        cursor2 = conn2.cursor()
                        cursor2.execute("SELECT computed FROM mapchunks WHERE mapID = %s", (uuid,))
                        status_result = cursor2.fetchone()
                        cursor2.close()
                        conn2.close()

                        if status_result and status_result[0] == 1:
                            print(f"Computation complete for UUID {uuid}")
                            break
                    except mysql.connector.Error as err:
                        print(f"MySQL error (status DB) for UUID {uuid}: {err}")

                    if time.time() - start_time > MAX_WAIT_TIME:
                        print(f"Timeout waiting for completion for UUID {uuid}. Moving to next.")
                        break

                    time.sleep(STATUS_POLL_INTERVAL)

            # --- Step 5: Append UUID and DB value to CSV row ---
            while len(row) < len(headers):
                row.append('')
            row[headers.index(UUID_COLUMN_NAME)] = uuid
            row[headers.index(DB_VALUE_COLUMN_NAME)] = db_value

            updated_rows.append(row)

# --- Step 6: Write updated CSV ---
with open(CSV_PATH, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(updated_rows)

print("CSV fully processed.")
