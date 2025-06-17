import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
import numpy as np
from scipy.optimize import curve_fit

def logistic_function(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

def plot_experiment_data(csv_file, start_index=0, end_index=None, points_only=False,
                         run_columns=None, poly_degree=2, average_runs=False,
                         regression_type="poly"):
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
        run_columns = [col.lower() for col in run_columns]
        for run_col in run_columns:
            if run_col not in df.columns:
                sys.exit(f"Run column '{run_col}' not found in CSV.")

    # Convert numeric
    df['size'] = pd.to_numeric(df['size'], errors='coerce')
    for run_col in run_columns:
        df[run_col] = pd.to_numeric(df[run_col], errors='coerce')

    df = df.dropna(subset=['size'])


    # Group by parts and worker
    groups = list(df.groupby(['parts', 'worker']))

    if end_index is None:
        end_index = len(groups)
    selected_groups = groups[start_index:end_index]

    plt.figure(figsize=(12, 8))

    for (parts, worker), group in selected_groups:
        label_base = f"{parts} - {worker}"

        if average_runs:
            x = group['size'].values
            run_data = group[run_columns].values
            y = np.nanmean(run_data, axis=1)

            mask = ~np.isnan(x) & ~np.isnan(y)
            x_clean = x[mask]
            y_clean = y[mask] / 1000

            if len(x_clean) < 2:
                continue

            label = f"{label_base} - avg({', '.join(run_columns)})"
            marker = 'o'

            if points_only:
                plt.scatter(x_clean, y_clean, label=label, marker=marker)
            else:
                plt.plot(x_clean, y_clean, label=label, linestyle='-', marker=marker)

            fit_and_plot_regression(x_clean, y_clean, regression_type, poly_degree, label)
        else:
            for i, run_col in enumerate(run_columns):
                x = group['size'].values
                y = group[run_col].values

                mask = ~np.isnan(x) & ~np.isnan(y)
                x_clean = x[mask]
                y_clean = y[mask]

                if len(x_clean) < 2:
                    continue

                original_label = col_map.get(run_col, run_col)
                label = f"{label_base} - {original_label}"
                marker = 'o' if i % 2 == 0 else 'x'
                linestyle = '-' if not points_only else 'None'

                if points_only:
                    plt.scatter(x_clean, y_clean, label=label, marker=marker)
                else:
                    plt.plot(x_clean, y_clean, label=label, linestyle=linestyle, marker=marker)

                fit_and_plot_regression(x_clean, y_clean, regression_type, poly_degree, label)

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
    #plt.yscale('log')
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()


def fit_and_plot_regression(x_clean, y_clean, regression_type, poly_degree, label):
    try:
        if regression_type == "poly":
            coeffs = np.polyfit(x_clean, y_clean, deg=poly_degree)
            fit_fn = np.poly1d(coeffs)
            y_fit = fit_fn(x_clean)

            # R²
            ss_res = np.sum((y_clean - y_fit) ** 2)
            ss_tot = np.sum((y_clean - np.mean(y_clean)) ** 2)
            r_squared = 1 - ss_res / ss_tot if ss_tot != 0 else 0

            # Plot
            x_sorted = np.sort(x_clean)
            y_sorted_fit = fit_fn(x_sorted)
            plt.plot(x_sorted, y_sorted_fit, linestyle='--', linewidth=1.5, alpha=0.7,
                     label=f"Fit: {label} (poly, R²={r_squared:.2f})")

            # Annotate equation
            equation_terms = []
            for j, coef in enumerate(coeffs[::-1]):
                power = j
                if abs(coef) < 1e-6:
                    continue
                if power == 0:
                    equation_terms.append(f"{coef:.2f}")
                elif power == 1:
                    equation_terms.append(f"{coef:.2f}x")
                else:
                    equation_terms.append(f"{coef:.2f}x^{power}")
            equation = " + ".join(equation_terms).replace('+ -', '- ')
        else:  # logistic
            p0 = [np.max(y_clean), 1, np.median(x_clean)]
            params, _ = curve_fit(logistic_function, x_clean, y_clean, p0=p0, maxfev=10000)
            fit_fn = lambda x: logistic_function(x, *params)
            y_fit = fit_fn(x_clean)

            ss_res = np.sum((y_clean - y_fit) ** 2)
            ss_tot = np.sum((y_clean - np.mean(y_clean)) ** 2)
            r_squared = 1 - ss_res / ss_tot if ss_tot != 0 else 0

            x_sorted = np.sort(x_clean)
            y_sorted_fit = fit_fn(x_sorted)
            plt.plot(x_sorted, y_sorted_fit, linestyle='--', linewidth=1.5, alpha=0.7,
                     label=f"Fit: {label} (logistic, R²={r_squared:.2f})")

            L, k, x0 = params
            equation = f"{L:.2f} / (1 + exp(-{k:.2f}(x - {x0:.2f})))"

        # Display equation on plot
        text_x = x_sorted[-1]
        text_y = y_sorted_fit[-1]
        plt.text(text_x, text_y, f"$y = {equation}$", fontsize=8, ha='right', va='bottom', alpha=0.7)
    except Exception as e:
        print(f"Failed to fit {regression_type} regression for {label}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot experimental data from a CSV file.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--start", type=int, default=0, help="Start index of groups to plot")
    parser.add_argument("--end", type=int, default=None, help="End index of groups to plot")
    parser.add_argument("--points-only", action="store_true", help="Plot only points (no lines)")
    parser.add_argument("--runs", nargs="+", help="Specify which Run columns to include (e.g. run1 Run2 RUN3)")
    parser.add_argument("--poly-degree", type=int, default=2, help="Degree of polynomial regression (if used)")
    parser.add_argument("--average-runs", action="store_true", help="Plot the average of all selected runs instead of each run individually")
    parser.add_argument("--regression-type", choices=["poly", "logistic"], default="poly",
                        help="Type of regression to fit: 'poly' or 'logistic' (default: poly)")

    args = parser.parse_args()

    plot_experiment_data(
        csv_file=args.csv_file,
        start_index=args.start,
        end_index=args.end,
        points_only=args.points_only,
        run_columns=args.runs,
        poly_degree=args.poly_degree,
        average_runs=args.average_runs,
        regression_type=args.regression_type
    )
