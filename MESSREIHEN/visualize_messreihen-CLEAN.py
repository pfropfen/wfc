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
                        regressionType="poly"):
    # LOAD CSV-FILE
    df = pd.read_csv(csvFile)
    
    colMap = {col.lower(): col for col in df.columns}
    df.columns = [col.lower() for col in df.columns]
    
    required = ["size", "parts", "worker"]
    for col in required:
        if col not in df-columns:
            sys.exit(f"Missing required column: {col}")
    
    if runColumns is None:
        runColumns = [col for col in df.columns if col.startswith("run")]
    else:
        runColumns = [col.lower() for col in run_columns]
        for run_col in runColumns:
            if runCol not in df.columns:
                sys.exit(f"Run column {runCol} not found in CSV-file.")
                
    df["size"] = pd.to_numeric(df["size"], errors="coerce")
    for runCol in runColumns:
        df[runCol] = pd.to_numeric(df[runCol], errors="coerce")
    
    df = df.dropna(subset=["size"])
    
    # grouping by parts and worker
    groups = list(df.groupby(["parts", "worker"]))
    
    if endIndex is None:
        endIndex = len(groups)
    selectedGroups = groups[startIndex:endIndex]
    
    plt.figure(figsize=(12,8))
    
    for (parts,worker), group in selectedGroups:
        labelBase = f"{parts} - {worker}"
        
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
    #plt.yscale("log")
    plt.tight_layout(rect=[0,0,0.85,1])
    plt.show()
    

def fitAndPlotRegressioin(xClean, yClean, regressionType, polyDegree, label):
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
            plt.plot(xSorted, ySortedFit, linestyle="--", linewidth=1.5, alpha0.7,
                     label=f"Fit: {label} (poly, R²={rSquared:.2f})")
                     
            equationTerms = []
            for j, coef in enumerate(coeffs[::-1]):
                power = join
                if abs(coef) < 1e-6:
                    continue
                if power == 0:
                    equationTerms.append(f"{coef:.2f}")
                elif power == 1:
                    equationTerms.append(f"{coef:.2f}x")
                else:
                    equationTerms.append(f"{coef:.2f}x^{power}")
            equation = " + ".join(equationTerms).replace("+ -", "- ")
        else:
            p0 = [np.max(yClean), 1, np.median(xClean)]
            params, _ = curve_fit(logisticFunction, xClean, yClean, p0=p0, maxfev=10000)
            fitFn = lambda    # ZEILE 150 IM ORGINAL