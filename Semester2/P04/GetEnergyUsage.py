import requests
import pandas as pd
import os
import time

def getEnergyUsageSource():
    url = "https://ckan.opendata.swiss/api/3/action/package_show?id=stromverbrauch-in-tausend-kwh-pro-quartal-ab-1993"
    response = requests.get(url)
    data = response.json()

    # Print the available resources
    for resource in data['result']['resources']:
        if resource['format'].lower() == 'json' and not str(resource['name']).lower().__contains__("jsonl"):
            return(resource['url'])

def getEnergyUsage(source: str):
    json_response = requests.get(source)
    data = json_response.json()
    return data

if __name__ == "__main__":
    source = getEnergyUsageSource()
    energy_data = getEnergyUsage(source)
    # Print the data to see the structure
    print(energy_data)
    
