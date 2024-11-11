from WRImprovement import WRImprovement
from UI import WRImprovementApp
from tkinter import *
from createTMNFWRHistory import SaveWRHistoryAsJson
import pickle

AutoSavesFolder = "C:/Users/Tobias/Documents/TrackMania/Tracks/Replays/Autosaves/"

def loadWRHistory() -> list[WRImprovement]:
    with open("WRHistory.pkl", "rb") as file:
        WRHistory = pickle.load(file)
    return WRHistory

def saveWRHistory(data: list[WRImprovement]):
    with open("WRHistory.pkl", "wb") as file:
        file.write(data)

if __name__ == "__main__":
    # SaveWRHistoryAsJson()
    WRHistory = loadWRHistory()

    root = Tk()
    app = WRImprovementApp(root, WRHistory)
    root.mainloop()

    saveWRHistory(pickle.dumps(WRHistory))