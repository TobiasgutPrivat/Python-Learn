from createTMNFWRHistory import getTMNFTracks
from WRImprovement import WRImprovement

class WRHistoryChallenge:
    WRImprovements: list[WRImprovement]
    currentPBs: dict[str, int | None]
    selectedWRImprovementIndex: int = 0

    def __init__(self, WRImprovements: list[WRImprovement]):
        self.WRImprovements = WRImprovements
        self.currentPBs = {}
        for track in getTMNFTracks():
            self.currentPBs[track["TrackName"]] = None

    def selectNextUnbeatenWRImprovement(self) -> None:
        for i in range(self.selectedWRImprovementIndex + 1, len(self.WRImprovements)):
            improvement = self.WRImprovements[i]
            if improvement.replay_time <= self.currentPBs[improvement.track_name]:
                self.selectedWRImprovementIndex = self.WRImprovements.index(improvement)
                return
        print("No unbeaten WR Improvements found")
    
    def GetSkippedWRImprovements(self) -> list[WRImprovement]:
        skippedWRImprovements = []
        for i in range(self.selectedWRImprovementIndex):
            improvement = self.WRImprovements[i]
            if improvement.replay_time > self.currentPBs[improvement.track_name]:
                skippedWRImprovements.append(improvement)
        return skippedWRImprovements
            
    def playSelectedWRImprovement(self) -> None:
        self.WRImprovements[self.selectedWRImprovementIndex].playAgainst()

    def getSelectedWRImprovementInfo(self) -> tuple[str, str, str, int | None]:
        improvement = self.WRImprovements[self.selectedWRImprovementIndex]
        return (improvement.track_name, improvement.user_name, improvement.formated_replay_time(), self.currentPBs[improvement.track_name])
    
    def setCurrentPB(self, replayTime: int) -> None:
        self.currentPBs[self.WRImprovements[self.selectedWRImprovementIndex].track_name] = replayTime

    def GetNextUnbeatenWRImprovements(self) -> list[WRImprovement]:
        nextUnbeatenWRImprovements = []
        for i in range(self.selectedWRImprovementIndex + 1, len(self.WRImprovements)):
            improvement = self.WRImprovements[i]
            if self.currentPBs[improvement.track_name] == None or improvement.replay_time <= self.currentPBs[improvement.track_name]:
                nextUnbeatenWRImprovements.append(improvement)
        return nextUnbeatenWRImprovements
