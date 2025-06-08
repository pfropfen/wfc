import pandas as pd
import matplotlib.pyplot as plt

def plot_experiment_data(csv_file):
    # Load the merged CSV file
    df = pd.read_csv(csv_file)

    # Rename columns for clarity
    df.columns = ['Size', 'Parts', 'Worker', 'Run1', 'Run2']

    # Convert relevant columns to numeric (errors='coerce' turns bad data into NaN)
    df['Size'] = pd.to_numeric(df['Size'], errors='coerce')
    df['Run1'] = pd.to_numeric(df['Run1'], errors='coerce')
    df['Run2'] = pd.to_numeric(df['Run2'], errors='coerce')

    # Drop rows missing Size
    df = df.dropna(subset=['Size'])

    # Group by Parts and Worker
    groups = df.groupby(['Parts', 'Worker'])

    plt.figure(figsize=(12, 8))

    for (parts, worker), group in groups:
        label_base = f"{parts} - {worker}"
        plt.plot(group['Size'], group['Run1'], label=f"{label_base} - Run1", linestyle='-', marker='o')
        #plt.plot(group['Size'], group['Run2'], label=f"{label_base} - Run2", linestyle='--', marker='x')

    plt.xlabel('Size')
    plt.ylabel('Measurement')
    plt.title('Experiment Results by Parts & Worker')
    plt.legend(loc='best', fontsize='small')
    plt.grid(True)
    
    plt.legend(
    loc='center left',
    bbox_to_anchor=(1.0, 0.5),
    fontsize='small',
    title='Legend'
    )

    plt.yscale('log')

    plt.tight_layout(rect=[0, 0, 0.85, 1])  # Reserve right margin for legend
    
    plt.show()

# Example usage:
plot_experiment_data('merged_messreihen.csv')
