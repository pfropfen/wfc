import csv

# File paths
mapids_file = "filtered_mapIDs.csv"
second_input_file = "chunkTimes.csv"
second_output_file = "cleaned_chunkTimes.csv"

# Load filtered mapIDs into a set for fast lookup
with open(mapids_file, mode='r', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    mapids_to_exclude = {row[0] for row in reader}

# Filter the second input file
with open(second_input_file, mode='r', newline='') as f_in, \
     open(second_output_file, mode='w', newline='') as f_out:

    reader = csv.reader(f_in)
    writer = csv.writer(f_out)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        if row and row[0] not in mapids_to_exclude:
            writer.writerow(row)

print("Rows with excluded mapIDs have been removed.")
