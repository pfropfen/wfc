import requests
from bs4 import BeautifulSoup
import mysql.connector
import csv
import time
import threading
import keyboard
import sys

baseIP = "139.6.65.27"

db1Config = {
    "host": baseIP,
    "port": 31006,
    "user": "wfc",
    "password": "wfc",
    "database": "times"
}

db2Config = {
    "host": baseIP,
    "port": 31007,
    "user": "wfc",
    "password": "wfc",
    "database": "maps"
}

rabbitmqUser = "guest"
rabbitmqPassword = "guest"
rabbitmqQueue = "maptickets"
rabbitmqApiUrl = f"http://{baseIP}:31672/api/queues/%2F/{rabbitmqQueue}"

def isQueueEmpty():
    try:
        response = requests.get(rabbitmqApiUrl, auth=(rabbitmqUser, rabbitmqPassword))
        if response.ok:
            data = response.json()
            messages = data.get("messages", -1)
            print(f"Queue '{rabbitmqQueue}' has {messages} messages.")
            return messages == 0
        else:
            print(f"Failed to get queue status: {response.status_code} {response.text}")
            return False
    except Exception as e:
        print(f"Error checking RabbitMQ queue: {e}")
        return False

numberOfWorkers = int(sys.argv[1])

csvPath = "messreihen.csv"
uuidColumnName = "uuid"
dbValueColumnName = "total"
statusPollInterval = 5
maxWaitTime = 1200

exitRequested = False
immediateExitRequested = False

def watchForExit():
    global exitRequested
    print("Press 'X' to stop the script gracefully.")
    keyboard.wait("x")
    print("\nExit requested. Finishing current row and saving...")
    exitRequested = True
    
def watchForImmediateExit():
    global immediateExitRequested
    print("Press 'Q' to stop the script gracefully immediately.")
    keyboard.wait("q")
    print("\nExit requested. saving ...")
    immediateExitRequested = True
    
threading.Thread(target=watchForExit, daemon=True).start()
threading.Thread(target=watchForImmediateExit, daemon=True).start()

updatedRows = []
with open(csvPath, mode="r", newline="") as file:
    reader = csv.reader(file)
    headers = next(reader)
    
    if uuidColumnName not in headers:
        headers.append(uuidColumnName)
    if dbValueColumnName not in headers:
        headers.append(dbValueColumnName)
    
    for rowIndex, row in enumerate(reader, start=1):
        if exitRequested:
            updatedRows.append(row)
            break
        
        print("Row: ", row)
        if int(row[2]) == numberOfWorkers and (len(row) < 7 or row[6].strip() == ""):
            payload = {
                "var1": str(row[0]),
                "var2": str(row[1]),
                "var3": "0",
                "var4": str(row[2])
            }
            
            response = requests.post(f"http://{baseIP}:31000/setRules", data=payload)
            time.sleep(30)
            
            try:
                response = requests.post(f"http://{baseIP}:31001/mapGenerator")
                if response.ok:
                    soup = BeautifulSoup(response.text, "html.parser")
                    uuidTag = soup.h1
                    uuid = uuidTag.text.strip() if uuidTag else ""
                else:
                    uuid = ""
            except Exception as e:
                print(f"Error during POST for row {rowIndex}: {e}")
                uuid = ""
            
            dbValue = ""
            if uuid:
                startTime = time.time()
                while True:
                    if immediateExitRequested:
                        break
                    try:
                        conn2 = mysql.connector.connect(**db2Config)
                        cursor2 = conn2.cursor()
                        cursor2.execute("SELECT mapID FROM mapchunks WHERE mapID = %s GROUP BY mapID HAVING SUM(CASE WHEN computed IS NOT TRUE THEN 1 ELSE 0 END) = 0", (uuid,))
                        
                        statusResult = cursor2.fetchone()
                        cursor2.close()
                        conn2.close()
                        
                        if statusResult:
                            print(f"Computation complete for UUID {uuid}")
                            
                            print("Waiting for RabbitMQ queue to empty...")
                            while not isQueueEmpty():
                                if immediateExitRequested:
                                    break
                                time.sleep(5)
                            print("RabbitMQ queue is empty. Continuing...")
                            
                            break
                    except mysql.connector.Error as err:
                        print(f"MySQL error (status DB) for UUID {uuid}: {err}")
                        
                    time.sleep(statusPollInterval)
                    try:
                        conn1 = mysql.connector.connect(**db1Config)
                        cursor1 = conn1.cursor()
                        cursor1.execute("SELECT totalDuration FROM mapTimes WHERE mapID = %s LIMIT 1", (uuid,))
                        result = cursor1.fetchone()
                        dbValue = result[0] if result else ""
                        cursor1.close()
                        conn1.close()
                    except mysql.connector.Error as err:
                        print(f"MySQL error (main DB) for UUID {uuid}: {err}")
                        dbValue = ""
                
                if immediateExitRequested:
                    updatedRows.append(row)
                    break
                
                while len(row) < len(headers):
                    row.append("")
                row[headers.index(uuidColumnName)] = uuid
                row[headers.index(dbValueColumnName)] = dbValue
            
            updatedRows.append(row)
        
        for remainingRow in reader:
            updatedRows.append(remainingRow)

with open(csvPath, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(updatedRows)

print("CSV fully processed.")