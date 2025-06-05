import csv

# Define file names
input_file = "mapTimes.csv"
filtered_mapids_file = "filtered_mapIDs.csv"
cleaned_file = "cleaned_mapTimes.csv"

# Containers
filtered_mapids = []
cleaned_rows = []

# Read and filter
with open(input_file, mode='r', newline='') as infile:
    reader = csv.reader(infile)
    header = next(reader)  # Read header
    cleaned_rows.append(header)

    for row in reader:
        if len(row) >= 4:
            if row[3] == '64':
                filtered_mapids.append([row[0]])  # Save mapID
            else:
                cleaned_rows.append(row)

# Write filtered mapIDs
with open(filtered_mapids_file, mode='w', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerow(['mapID'])
    writer.writerows(filtered_mapids)

# Write cleaned data without rows where numberOfWorkers == 64
with open(cleaned_file, mode='w', newline='') as f_out:
    writer = csv.writer(f_out)
    writer.writerows(cleaned_rows)

print("Filtering complete.")
