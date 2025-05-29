import pandas as pd
import matplotlib.pyplot as plt

# === Config ===
SMOOTHING_ENABLED = True   # Toggle smoothing on/off
SMOOTHING_WINDOW = 3        # Rolling average window size
MAX_LINES = 0               # Set to 0 or less to show all lines
MIN_DATAPOINTS = 1          # Minimum number of datapoints per group

# Load and clean data
df = pd.read_csv('merged_sorted_output.csv')
df.columns = ['col1', 'mapSize', 'chunkCount', 'numberOfWorkers', 'col5', 'col6', 'time_ms']

df['time_ms'] = pd.to_numeric(df['time_ms'], errors='coerce')
df['mapSize'] = pd.to_numeric(df['mapSize'], errors='coerce')
df = df.dropna(subset=['time_ms', 'mapSize'])
df = df[df['time_ms'] > 0]

# Plot setup
plt.figure(figsize=(12, 8))

# Group data
grouped = list(df.groupby(['chunkCount', 'numberOfWorkers']))
if MAX_LINES > 0:
    grouped = grouped[:MAX_LINES]

# Plot each group with ≥ MIN_DATAPOINTS
for (chunkCount, numberOfWorkers), group in grouped:
    group = group.sort_values(by='mapSize')  # Sort by x-axis

    if SMOOTHING_ENABLED:
        smoothed = group[['mapSize', 'time_ms']].rolling(window=SMOOTHING_WINDOW, center=True).mean().dropna()
        if len(smoothed) < MIN_DATAPOINTS:
            continue
        x = smoothed['mapSize']
        y = smoothed['time_ms']
        num_points = len(smoothed)
    else:
        if len(group) < MIN_DATAPOINTS:
            continue
        x = group['mapSize']
        y = group['time_ms']
        num_points = len(group)

    label = f'chunks={chunkCount}, workers={numberOfWorkers} ({num_points} pts)'
    plt.plot(x, y, label=label)

# Axes and formatting
plt.yscale('log')  # log scale on new y-axis (was x before)
plt.xlim(left=0)   # Ensure x-axis starts at 0 if needed

plt.xlabel('Map Size')
plt.ylabel('Time (ms) [log scale]')
plt.title('Time over Map Size by Chunk & Worker Count' + (' [Smoothed]' if SMOOTHING_ENABLED else ''))
plt.legend(title='Configurations', fontsize=9)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Show the plot
plt.show()
