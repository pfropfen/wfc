import csv

def remove_last_two_columns(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            writer.writerow(row[:-2])  # Remove the last two columns

# Example usage:
input_csv = 'messreihen_clean.csv'
output_csv = 'messreihen_clean2.csv'
remove_last_two_columns(input_csv, output_csv)
