from WRImprovement import WRImprovement
from UI import WRImprovementUI
import tkinter as tk
from createTMNFWRHistory import SaveWRHistoryAsJson
import pickle

def loadWRHistory() -> list[WRImprovement]:
    with open("WRHistory.pkl", "rb") as file:
        WRHistory = pickle.load(file)
    return WRHistory

def saveWRHistory(data: list[WRImprovement]):
    with open("WRHistory.pkl", "wb") as file:
        file.write(data)

if __name__ == "__main__":
    WRHistory = loadWRHistory()

    root = tk.Tk()
    app = WRImprovementUI(root, WRHistory)

    root.mainloop()

    saveWRHistory(pickle.dumps(WRHistory))