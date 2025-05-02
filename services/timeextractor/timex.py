import mysql.connector
import csv
import os

def export_database_to_csv(host, user, password, database, port=3306, output_dir="output"):
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )
    cursor = conn.cursor()
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get all tables in the database
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    
    for (table_name,) in tables:
        print(f"Exporting {table_name}...")
        
        # Fetch all data from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        column_names = [desc[0] for desc in cursor.description]
        
        # Define CSV file path
        csv_file_path = os.path.join(output_dir, f"{table_name}.csv")
        
        # Write data to CSV
        with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(column_names)  # Write headers
            writer.writerows(rows)         # Write data
        
        print(f"{table_name} exported successfully to {csv_file_path}")
    
    # Close connection
    cursor.close()
    conn.close()
    print("Database export completed.")

# Connection to DB
export_database_to_csv(host="192.168.178.56", user="root", password="root", database="times", port=31006)