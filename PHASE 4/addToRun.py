import csv

# File paths
file1 = 'Run3/messreihen.csv'  # This file will be updated
file2 = 'Run3 add/messreihen.csv'  # This file contains new values to insert

results_map = {}
with open(file2, newline='') as f2:
    reader = csv.reader(f2)
    for row in reader:
        key = tuple(row[:5])     # Key = first 5 columns
        values = row[5:7]        # Values = 6th and 7th columns to insert
        results_map[key] = values

# Step 2: Read the first file and append the matching values from the second file
updated_rows = []
with open(file1, newline='') as f1:
    reader = csv.reader(f1)
    for row in reader:
        key = tuple(row[:5])
        values_to_add = results_map.get(key, ['', ''])  # Default to blanks if not found
        updated_row = row + values_to_add               # Append the two values
        updated_rows.append(updated_row)

# Save updated data back to file1 or to a new file
with open('Run3/messreihen_complete.csv', 'w', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(updated_rows)

print("Merge complete. Output saved to 'merged_output.csv'")
