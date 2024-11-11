# from WRHistoryChallenge import WRHistoryChallenge
from WRImprovement import WRImprovement
import ttkbootstrap as ttk
# from createTMNFWRHistory import GetTMNFWRHistory
from UI import WRHistoryChallengeUI
import pickle

def loadWRHistoryChallenge() -> list[WRImprovement]:
    with open("WRHistoryChallenge.pkl", "rb") as file:
        WRHistory = pickle.load(file)
    return WRHistory

def saveWRHistoryChallenge(data: list[WRImprovement]):
    with open("WRHistoryChallenge.pkl", "wb") as file:
        file.write(data)

if __name__ == "__main__":
    wRHistoryChallenge = loadWRHistoryChallenge()
    # wRHistoryChallenge = WRHistoryChallenge(GetTMNFWRHistory())

    root = ttk.Window()
    WRHistoryChallengeUI(root, wRHistoryChallenge)

    root.mainloop()

    saveWRHistoryChallenge(pickle.dumps(wRHistoryChallenge))