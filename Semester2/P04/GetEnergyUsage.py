import pandas as pd

def getEnergyUsageSource():
    """Fetch the API URL for energy usage data."""
    url = "https://ckan.opendata.swiss/api/3/action/package_show?id=stromverbrauch-in-tausend-kwh-pro-quartal-ab-1993"
    data = pd.read_json(url)  # Fetch API metadata directly
    for resource in data["result"]["resources"]:
        if any([format == "json" for format in resource["name"].values()]):
            return resource["url"]
    return None

def getEnergyUsage(source: str):
    """Load JSON data directly from the API into a Pandas DataFrame."""
    df = pd.read_json(source)
    return df

if __name__ == "__main__":
    source = getEnergyUsageSource()
    print(f"Data source URL: {source}")
    if source:
        df = getEnergyUsage(source)
        print(df.head())  # Display the first few rows
    else:
        print("No valid data source found.")
