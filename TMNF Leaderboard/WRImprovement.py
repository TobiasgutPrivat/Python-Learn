from datetime import datetime
from dataclasses import dataclass
import requests
import os

@dataclass
class WRImprovement:
    replay_id: int
    replay_time: int
    user_name: str
    replay_at: str
    track_name: str
    beaten: bool
    ReplayPath: str

    def DownloadReplay(self):
        url = f"https://tmnf.exchange/recordgbx/{self.replay_id}"
        response = requests.get(url)

        if response.status_code == 200:
            with open(self.ReplayPath + "replay.gbx", "wb") as file:
                file.write(response.content)

    def playAgainst(self):
        if not os.path.exists(self.ReplayPath + "replay.gbx"):
            self.DownloadReplay()
        
        os.startfile(self.ReplayPath + "replay.gbx")# windows only

    def registerBeaten(self, AutoSavesFolder: str) -> bool:
        for file in os.listdir(AutoSavesFolder):
            if file.endswith(".gbx"):
                if file.__contains__("TrackName"):
                    self.beaten = True
                    os.rename(AutoSavesFolder + file, self.ReplayPath + os.path.basename(AutoSavesFolder + file))
        


def format_replay_time(ms: int) -> str:
    seconds, milliseconds = divmod(ms, 1000)

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    formatted_time = (f"{hours:02}:" if hours > 0 else "") + (f"{minutes:02}:" if minutes > 0 else "") + f"{seconds:02}.{int(milliseconds/10):02}"
    return formatted_time
