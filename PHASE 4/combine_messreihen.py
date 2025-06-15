import csv

def read_csv_conditions_measurement(filepath):
    data = {}
    missing_keys = set()

    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header
        for row in reader:
            if len(row) < 3:
                continue  # Ignore malformed rows
            key = tuple(row[:3])
            value = row[6] if len(row) > 6 else ''
            if value == '':
                missing_keys.add(key)
            data[key] = value
    return data, missing_keys

def merge_multiple_csv_files(filepaths, output_file, missing_output):
    all_data = []
    all_keys = set()
    all_missing = []  # List of (condition tuple, filename)

    for path in filepaths:
        data, missing_keys = read_csv_conditions_measurement(path)
        all_data.append(data)
        all_keys.update(data.keys())
        all_missing.extend((key, path) for key in missing_keys)

    # Sorting all keys numerically
    def sort_key(key_tuple):
        return tuple(int(k) for k in key_tuple)

    # Write merged output
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        header = ['SIZE', 'PARTS', 'WORKER']
        header += [f'Run{i+1}' for i in range(len(filepaths))]
        writer.writerow(header)

        for key in sorted(all_keys, key=sort_key):
            row = list(key)
            for data in all_data:
                row.append(data.get(key, ''))
            writer.writerow(row)

    # Write missing values report
    with open(missing_output, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['SIZE', 'PARTS', 'WORKER', 'MissingInFile'])
        for key, filename in sorted(all_missing, key=lambda x: sort_key(x[0])):
            writer.writerow(list(key) + [filename])

# Example usage:
merge_multiple_csv_files(
    ['RUN1/messreihen_complete.csv', 'RUN2/messreihen_complete.csv', 'RUN3/messreihen_complete.csv'],
    'merged_messreihen.csv',
    'missing_values.csv'
)
