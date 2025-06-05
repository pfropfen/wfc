import requests
from bs4 import BeautifulSoup
import csv
import time
import sys


# --- DB configurations ---
DB1_CONFIG = {
    'host': '139.6.65.27',
    'port': 31006,
    'user': 'wfc',
    'password': 'wfc',
    'database': 'times'
}

DB2_CONFIG = {
    'host': '139.6.65.27',
    'port': 31007,
    'user': 'wfc',
    'password': 'wfc',
    'database': 'maps'
}

numberOfWorkers = int(sys.argv[1])

# --- Constants ---
CSV_PATH = 'messreihen.csv'
UUID_COLUMN_NAME = 'uuid'
DB_VALUE_COLUMN_NAME = 'total'
STATUS_POLL_INTERVAL = 5  # seconds between status checks
MAX_WAIT_TIME = 1200        # max seconds to wait per row

# --- Exit flag ---
exit_requested = False
immediate_exit_requested = False



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
    
        if int(row[2]) == numberOfWorkers and (len(row) < 7 or row[6].strip() == ''):
            print(row)