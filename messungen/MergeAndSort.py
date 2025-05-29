import pandas as pd
import glob

# List of your CSV file paths (replace these with your actual file names or use a pattern)
csv_files = [
    'phase2-1/mapTimes.csv',
    'phase2-2 (16 worker)/mapTimes.csv',
    'phase 2-3 (32 worker)/mapTimes.csv',
    'phase2-4 (64 worker)/mapTimes.csv',
    'phase2-5 (128 worker)/mapTimes.csv',
    'phase2-6/mapTimes.csv'
]

# Read and concatenate all CSV files into one DataFrame
all_dataframes = []
for file in csv_files:
    df = pd.read_csv(file)
    if df.shape[1] != 7:
        raise ValueError(f"{file} does not have exactly 7 columns.")
    all_dataframes.append(df)

merged_df = pd.concat(all_dataframes, ignore_index=True)

# Drop rows where the last column is NaN or empty string
last_col = merged_df.columns[-1]
merged_df[last_col] = pd.to_numeric(merged_df[last_col], errors='coerce')
merged_df = merged_df[merged_df[last_col].notna()]
merged_df = merged_df[merged_df[last_col].astype(str).str.strip() != ""]

# Sort by the last column (assuming values are sortable)
merged_df = merged_df.sort_values(by=last_col)

# Write to a new CSV file
merged_df.to_csv('merged_sorted_output.csv', index=False)

print("Merging and sorting complete. Output saved to 'merged_sorted_output.csv'.")
