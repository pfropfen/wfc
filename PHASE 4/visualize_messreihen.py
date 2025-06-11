import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys

def plot_experiment_data(csv_file, start_index=0, end_index=None, points_only=False, run_columns=None):
    # Load CSV
    df = pd.read_csv(csv_file)

    # Normalize column names to lowercase internally
    col_map = {col.lower(): col for col in df.columns}
    df.columns = [col.lower() for col in df.columns]

    # Ensure required columns exist
    required = ['size', 'parts', 'worker']
    for col in required:
        if col not in df.columns:
            sys.exit(f"Missing required column: {col}")

    # Auto-detect runs if not specified
    if run_columns is None:
        run_columns = [col for col in df.columns if col.startswith("run")]
    else:
        # Normalize user input and validate
        run_columns = [col.lower() for col in run_columns]
        for run_col in run_columns:
            if run_col not in df.columns:
                sys.exit(f"Run column '{run_col}' not found in CSV.")

    # Convert numeric
    df['size'] = pd.to_numeric(df['size'], errors='coerce')
    for run_col in run_columns:
        df[run_col] = pd.to_numeric(df[run_col], errors='coerce')

    # Drop rows missing size
    df = df.dropna(subset=['size'])

    # Group by parts and worker
    groups = list(df.groupby(['parts', 'worker']))

    if end_index is None:
        end_index = len(groups)
    selected_groups = groups[start_index:end_index]

    plt.figure(figsize=(12, 8))

    for (parts, worker), group in selected_groups:
        label_base = f"{parts} - {worker}"

        for i, run_col in enumerate(run_columns):
            original_label = col_map.get(run_col, run_col)  # use original case for legend
            label = f"{label_base} - {original_label}"
            marker = 'o' if i % 2 == 0 else 'x'
            linestyle = '-' if not points_only else 'None'

            if points_only:
                plt.scatter(group['size'], group[run_col], label=label, marker=marker)
            else:
                plt.plot(group['size'], group[run_col], label=label, linestyle=linestyle, marker=marker)

    plt.xlabel('Size')
    plt.ylabel('Measurement')
    plt.title('Experiment Results by Parts & Worker')
    plt.legend(
        loc='center left',
        bbox_to_anchor=(1.0, 0.5),
        fontsize='small',
        title='Legend'
    )
    plt.grid(True)
    plt.yscale('log')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot experimental data from a CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--start", type=int, default=0, help="Start index of groups to plot")
    parser.add_argument("--end", type=int, default=None, help="End index of groups to plot")
    parser.add_argument("--points-only", action="store_true", help="Plot only points (no lines)")
    parser.add_argument("--runs", nargs="+", help="Specify which Run columns to include (e.g. run1 Run2 RUN3)")

    args = parser.parse_args()

    plot_experiment_data(
        csv_file=args.csv_file,
        start_index=args.start,
        end_index=args.end,
        points_only=args.points_only,
        run_columns=args.runs
    )
