import csv

def detect_outliers(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header if your file has one; remove if not needed
        row_number = 2  # Because we skipped the header

        for row in reader:
            try:
                val1 = float(row[3])
                val2 = float(row[4])
                if val1 == 0 and val2 == 0:
                    continue  # avoid division by zero

                # Calculate percentage difference relative to the smaller of the two
                min_val = min(abs(val1), abs(val2))
                if min_val == 0:
                    continue  # avoid division by zero

                percent_diff = abs(val1 - val2) / min_val

                if percent_diff > 0.2:
                    print(f"Row {row_number}: {row}")
            except (ValueError, IndexError):
                pass
                #print(f"Skipping row {row_number}: unable to parse numbers or missing data")
            row_number += 1

# Example usage
detect_outliers("merged_messreihen.csv")
