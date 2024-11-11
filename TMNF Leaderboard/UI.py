from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from WRImprovement import WRImprovement

class WRImprovementApp:
    def __init__(self, root, improvements: list[WRImprovement]):
        self.root = root
        self.improvements = improvements
        self.style = Style("cosmo")  # Using the 'cosmo' theme for ttkbootstrap

        # Configure main window
        self.root.title("WR Improvement Tracker")
        self.root.geometry("800x400")

        # Create a Treeview widget
        self.tree = ttk.Treeview(root, columns=("ID", "Time", "User", "Date", "Track", "Beaten"), show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        # Define columns
        self.tree.heading("ID", text="Replay ID")
        self.tree.heading("Time", text="Replay Time")
        self.tree.heading("User", text="User Name")
        self.tree.heading("Date", text="Replay Date")
        self.tree.heading("Track", text="Track Name")
        self.tree.heading("Beaten", text="Beaten")

        # Insert data into Treeview
        for improvement in improvements:
            self.tree.insert("", END, values=(improvement.replay_id, improvement.replay_at.strftime("%Y-%m-%d"), improvement.user_name, 
                                              improvement.replay_at, improvement.track_name, improvement.beaten))

        # Add Buttons
        self.download_button = ttk.Button(root, text="Download Replay", command=self.download_selected_replay)
        self.download_button.pack(side=LEFT, padx=10, pady=10)

        self.play_button = ttk.Button(root, text="Play Against", command=self.play_selected_replay)
        self.play_button.pack(side=LEFT, padx=10, pady=10)

    def get_selected_improvement(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)["values"]
            replay_id = item_values[0]
            return next((imp for imp in self.improvements if imp.replay_id == replay_id), None)
        return None

    def download_selected_replay(self):
        selected_improvement = self.get_selected_improvement()
        if selected_improvement:
            selected_improvement.DownloadReplay()
            print("Replay downloaded.")

    def play_selected_replay(self):
        selected_improvement = self.get_selected_improvement()
        if selected_improvement:
            selected_improvement.playAgainst()
            print("Playing against replay.")