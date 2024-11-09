import requests
from datetime import datetime
from openpyxl import Workbook
from functools import lru_cache

@lru_cache(maxsize=0)
def getMapReplays(mapID: str, afterID: str = None) -> list:
    url = "https://tmnf.exchange/api/replays"
    params = {
        "fields": "ReplayId,ReplayTime,User.Name,ReplayAt",  # Select relevant fields
        "trackId": mapID,  # Replace with the actual track ID
        "count": 1000,
    }
    if afterID != None:
        params["after"] = afterID
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["Results"]
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")

def getAllReplays(mapID: str) -> list:
    AllReplays = []
    results = getMapReplays(mapID)

    AllReplays.extend(results)
    while len(results) == 1000:
        afterID = results[-1]["ReplayId"]
        lastResult = results
        results = getMapReplays(mapID, afterID)
        if lastResult == results:
            break
        AllReplays.extend(results)

    for replay in AllReplays:
        if '.' in replay["ReplayAt"]:
            replay["ReplayAt"] = datetime.strptime(replay["ReplayAt"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            replay["ReplayAt"] = datetime.strptime(replay["ReplayAt"], "%Y-%m-%dT%H:%M:%S")
    return AllReplays

def getAllWRImprovements(mapID: str) -> list:
    AllImprovements = []
    replays = getAllReplays(mapID)
    print(len(replays))
    replays.sort(key=lambda x: x["ReplayAt"])
    WR = 999999999
    for replay in replays:
        if replay["ReplayTime"] < WR:
            WR = replay["ReplayTime"]
            AllImprovements.append(replay)
    return AllImprovements

def GetTMNFWRHistory() -> list:
    url = "https://tmnf.exchange/api/tracks"
    params = {
        "fields": "TrackId,TrackName",  # Select relevant fields
        "author": "Nadeo",  # Replace with the actual track ID
        "count": 65,
        "after": "10369947" #last Beta Map ID 10369947
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        tracks = data["Results"]
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")
    
    AllWRImprovements = []
    for track in tracks:
        print(track["TrackName"])
        trackImprovements = getAllWRImprovements(track["TrackId"])
        for improvement in trackImprovements:
            improvement["TrackName"] = track["TrackName"]
        AllWRImprovements.extend(trackImprovements)
    return AllWRImprovements

def SaveWRHistory() -> None:
    # Create a new workbook and select the active worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "WRHistory"

    # Define the headers
    headers = ['TrackName', 'ReplayAt', 'ReplayTime', 'UserName', 'ReplayId']
    worksheet.append(headers)  # Write the headers to the first row

    # Populate the worksheet with data
    for entry in GetTMNFWRHistory():
        row = [
            entry['TrackName'],
            entry['ReplayAt'].strftime("%Y-%m-%d %H:%M:%S"),
            entry['ReplayTime'],
            entry['User']['Name'],
            entry['ReplayId']
        ]
        worksheet.append(row)  # Append each row to the worksheet
    workbook.save('WRHistory.xlsx')

if __name__ == "__main__":
    SaveWRHistory()