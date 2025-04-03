import requests
import os
import time
import json

cache_file = "EnergyUsage.json"
cache_time = 10 * 60  # 10 minutes in seconds

def getEnergyUsageSource():
    url = "https://ckan.opendata.swiss/api/3/action/package_show?id=stromverbrauch-in-tausend-kwh-pro-quartal-ab-1993"
    response = requests.get(url)
    data = response.json()

    # Print the available resources
    for resource in data['result']['resources']:
        if resource['format'].lower() == 'json' and not str(resource['name']).lower().__contains__("jsonl"):
            return(resource['url'])

def getEnergyUsage(source: str):
    if not os.path.exists(cache_file) or (time.time() - os.stat(cache_file).st_mtime) > cache_time:
        json_response = requests.get(source)
        data = json_response.json()
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    else:
        with open(cache_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    return data

if __name__ == "__main__":
    source = getEnergyUsageSource()
    energy_data = getEnergyUsage(source)
    # Print the data to see the structure
    print(energy_data)
    
