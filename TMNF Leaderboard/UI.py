from WRImprovement import WRImprovement
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

AutoSavesFolder = "C:/Users/Tobias/Documents/TrackMania/Tracks/Replays/Autosaves/"

class WRImprovementUI:
    def __init__(self, root, improvements):
        self.root = root
        self.improvements = improvements
        self.next_unbeaten_improvement = self.get_next_unbeaten_improvement()
        
        # Title of the window
        root.title("WR Improvements Viewer")
        
        # Frame to hold the improvements
        self.improvement_frame = tk.Frame(root)
        self.improvement_frame.pack(pady=10)

        # Listbox to display improvements
        self.listbox = tk.Listbox(self.improvement_frame, height=10, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self.improvement_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Add items to the listbox
        self.update_listbox()

        # Display the details of the selected improvement
        self.details_frame = tk.Frame(root)
        self.details_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Open the next unbeaten improvement by default
        if self.next_unbeaten_improvement:
            self.open_improvement(self.next_unbeaten_improvement)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for improvement in self.improvements:
            self.listbox.insert(tk.END, f"{improvement.user_name} - {improvement.track_name}")

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            selected_index = selection[0]
            improvement = self.improvements[selected_index]
            self.open_improvement(improvement)

    def open_improvement(self, improvement):
        # Clear the details frame
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        # Show the details of the selected improvement
        details_text = (
            f"User Name: {improvement.user_name}\n"
            f"Track Name: {improvement.track_name}\n"
            f"Replay Time: {improvement.formated_replay_time()}\n"
            f"Beaten: {'Yes' if improvement.beaten else 'No'}\n"
            f"Replay Path: {improvement.ReplayPath}"
        )
        
        details_label = tk.Label(self.details_frame, text=details_text, justify=tk.LEFT)
        details_label.pack()

        # Play button
        play_button = tk.Button(self.details_frame, text="Play Against", command=improvement.playAgainst)
        play_button.pack(pady=5)

        # Register beaten button
        register_button = tk.Button(self.details_frame, text="Register Beaten", command=lambda: self.register_beaten(improvement))
        register_button.pack(pady=5)

    def register_beaten(self, improvement: WRImprovement):
        # Example of handling register beaten functionality
        if improvement.registerBeaten(AutoSavesFolder):
            messagebox.showinfo("Success", f"Improvement {improvement.track_name} has been marked as beaten!")
        else:
            messagebox.showwarning("Failure", "No matching record found to beat this improvement.")

    def get_next_unbeaten_improvement(self):
        for improvement in self.improvements:
            if not improvement.beaten:
                return improvement
        return None
