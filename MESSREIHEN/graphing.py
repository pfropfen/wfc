import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys
import numpy as np
from scipy.optimize import curve_fit


def logisticFunction(x, L, k, x0):
    return L / (1 + np.exp(-k*(x-x0)))
    

def plotExperimentData(csvFile, startIndex=0, endIndex=None, pointsOnly=False,
                        runColumns=None, polyDegree=2, averageRuns=False,
                        regressionType="poly", selectedSizePerPart=None):
    # LOAD CSV-FILE
    df = pd.read_csv(csvFile)
    
    colMap = {col.lower(): col for col in df.columns}
    df.columns = [col.lower() for col in df.columns]
    
    required = ["size", "parts", "worker"]
    for col in required:
        if col not in df.columns:
            sys.exit(f"Missing required column: {col}")
    
    if runColumns is None:
        runColumns = [col for col in df.columns if col.startswith("run")]
    else:
        runColumns = [col.lower() for col in runColumns]
        for runCol in runColumns:
            if runCol not in df.columns:
                sys.exit(f"Run column {runCol} not found in CSV-file.")
                
    df["size"] = pd.to_numeric(df["size"], errors="coerce")
    for runCol in runColumns:
        df[runCol] = pd.to_numeric(df[runCol], errors="coerce")
    
    df = df.dropna(subset=["size"])
    
    df["size_per_part"] = (df["size"] ** 2) / df["parts"]
    
    if selectedSizePerPart is not None:
        df = df[df["size_per_part"].isin(selectedSizePerPart)]
    
    #groups = list(df.groupby(["size_per_part"]))
    groups = list(df.groupby(["parts", "worker"]))
    
    if endIndex is None:
        endIndex = len(groups)
    selectedGroups = groups[startIndex:endIndex]
    
    plt.figure(figsize=(14,8))
    
    for (parts, worker), group in selectedGroups:
        labelBase = f"{parts}-{worker}"
        
        if averageRuns:
            x=group["size"].values
            runData=group[runColumns].values
            y=np.nanmean(runData, axis=1)
            
            mask=~np.isnan(x) & ~np.isnan(y)
            xClean=x[mask]
            yClean=y[mask]/1000
            
            if len(xClean)<2:
                continue
            
            label=f"{labelBase}-avg({", ".join(runColumns)})"
            marker="o"
            
            if pointsOnly:
                plt.scatter(xClean, yClean, label=label, marker=marker)
            else:
                plt.plot(xClean, yClean, label=label, linestyle="-", marker=marker)
            
            fitAndPlotRegression(xClean, yClean, regressionType, polyDegree, label)
        else:
            for i, runCol in enumerate(runColumns):
                x=group["size"].values
                y=group[runCol].values
                
                mask=~np.isnan(x) & ~np.isnan(y)
                xClean=x[mask]
                yClean=y[mask]
                
                if len(xClean)<2:
                    continue
                    
                originalLabel = colMap.get(runCol, runCol)
                label = f"{labelBase} - {originalLabel}"
                marker = "o" if i % 2 == 0 else "x"
                linestyle = "-" if not pointsOnly else "None"
                
                if pointsOnly:
                    plt.scatter(xClean, yClean, label=label, marker=marker)
                else:
                    plt.plot(xClean, yClean, label=label, linestyle=linestyle, marker=marker)
                
                fitAndPlotRegression(xClean, yClean, regressionType, polyDegree, label)
    
    plt.xlabel("Size")
    plt.ylabel("Measurement")
    plt.title("Experiment Results by Parts & Worker")
    plt.legend(
        loc="center left",
        bbox_to_anchor=(1.0, 0.5),
        fontsize="small",
        title="Legend"
    )
    plt.grid(True)
    plt.yscale("log")
    plt.tight_layout(rect=[0,0,0.85,1])
    plt.show()
    

def fitAndPlotRegression(xClean, yClean, regressionType, polyDegree, label):
    try:
        if regressionType == "poly":
            coeffs = np.polyfit(xClean, yClean, deg=polyDegree)
            fitFn = np.poly1d(coeffs)
            yFit = fitFn(xClean)
            
            ssRes = np.sum((yClean-yFit)**2)
            ssTot = np.sum((yClean-np.mean(yClean))**2)
            rSquared = 1 - ssRes/ssTot if ssTot != 0 else 0
            
            xSorted = np.sort(xClean)
            ySortedFit = fitFn(xSorted)
                     
            equationTerms = []
            for j, coef in enumerate(coeffs[::-1]):
                power = j
                if abs(coef) < 1e-6:
                    continue
                if power == 0:
                    equationTerms.append(f"{coef:.7f}")
                elif power == 1:
                    equationTerms.append(f"{coef:.7f}x")
                else:
                    equationTerms.append(f"{coef:.7f}x^{power}")
            equation = " + ".join(equationTerms).replace("+ -", "- ")
            
            plt.plot(xSorted, ySortedFit, linestyle="--", linewidth=1.5, alpha=0.7,
                     label=f"Fit: {label} (R²={rSquared:.4f})\ny={equation:<70}")
        else:
            p0 = [np.max(yClean), 1, np.median(xClean)]
            params, _ = curve_fit(logisticFunction, xClean, yClean, p0=p0, maxfev=10000)
            fitFn = lambda x: logisticFunction(x, *params)
            yFit = fitFn(xClean)
            
            ssRes = np.sum((yClean - yFit) ** 2)
            ssTot = np.sum((yClean - np.mean(yClean)) ** 2)
            rSquared = 1 - ssRes / ssTot if ssTot != 0 else 0
            
            xSorted = np.sort(xClean)
            ySortedFit = fitFn(xSorted)
                    
            L, k, x0 = params
            equation = f"{L:.7f} / (1 + exp(-{k:.7f}(x - {x0:.7f})))"
            
            plt.plot(xSorted, ySortedFit, linestyle="--", linewidth=1.5, alpha=0.7,
                    label=f"Fit: {label} (R²={rSquared:.4f})\ny={equation}")
        
    except Exception as e:
        print(f"Failed to fit {regressionType} regression for {label}: {e}")

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
    parser.add_argument("--select-size-per-part", nargs="+", type=float, help="List of specific chunksizes to include")
    
    args = parser.parse_args()
    
    plotExperimentData(
        csvFile=args.csv_file,
        startIndex=args.start,
        endIndex=args.end,
        pointsOnly=args.points_only,
        runColumns=args.runs,
        polyDegree=args.poly_degree,
        averageRuns=args.average_runs,
        regressionType=args.regression_type,
        selectedSizePerPart=args.select_size_per_part
    )