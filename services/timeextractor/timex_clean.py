import mysql.connector
import csv
import os

def exportDatabaseToCsv(host, user, password, database, port=3306, outputDir="output"):
    
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    
    cursor = conn.cursor()
    
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    
    for (tableName,) in tables:
        print(f"Exporting {tableName}...")
        
        cursor.execute(f"SELECT * FROM {tableName}")
        rows = cursor.fetchall()
        
        columnNames = [desc[0] for desc in cursor.description]
        
        csvFilePath = os.path.join(outputDir, f"{tableName}.csv")
        
        with open(csvFilePath, mode="w", newline="", encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(columnNames)
            writer.writerows(rows)
            
        print(f"{tableName} exported successfully to {csvFilePath}")
    
    cursor.close()
    conn.close()
    print("Database export completed.")
    
exportDatabaseToCsv(host="139.6.65.27", user="root", password="root", database="times", port=31006)