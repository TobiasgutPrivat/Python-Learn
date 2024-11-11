from WRImprovement import WRImprovement
from createTMNFWRHistory import SaveWRHistoryAsJson
import pickle

AutoSavesFolder = "C:/Users/Tobias/Documents/TrackMania/Tracks/Replays/Autosaves"


def loadWRHistory() -> list:
    with open("WRHistory.pkl", "rb") as file:
        WRHistory = pickle.load(file)
    return WRHistory

if __name__ == "__main__":
    # SaveWRHistoryAsJson()
    WRHistory = loadWRHistory()

    for entry in WRHistory:
        print(entry)