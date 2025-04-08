from GetEnergyUsage import getEnergyUsage, getEnergyUsageSource
import matplotlib.pyplot as plt
import pandas as pd

def evaluateDataFrame(df: pd.DataFrame):
    """Create a line chart using a Pandas DataFrame."""
    if "date" not in df.columns or "conso_total" not in df.columns:
        print("Required columns not found in DataFrame.")
        return
    
    df["date"] = pd.to_datetime(df["date"])  # Convert date column to datetime
    df.sort_values("date", inplace=True)  # Ensure chronological order

    plt.figure(figsize=(10, 5))
    plt.plot(df["date"], df["conso_total"], marker='o', linestyle='-')

    plt.title("Energy Consumption in Fribourg")
    plt.xlabel("Quarter")
    plt.ylabel("MWh/Quarter")
    plt.xticks(rotation=45)  # Rotate labels for better readability
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    source = getEnergyUsageSource()
    if source:
        df = getEnergyUsage(source)
        evaluateDataFrame(df)  # Use the DataFrame for visualization
    else:
        print("No valid data source found.")
