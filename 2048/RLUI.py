import tkinter as tk
from game import Game2048
from constants import BACKGROUND_COLOR, EMPTY_CELL_COLOR, CELL_COLORS, TEXT_COLORS, FONT

class RLUI2048:
    window: tk.Tk
    step_label: tk.Label
    score_label: tk.Label
    frame: tk.Frame
    cells: list[list]
    def __init__(self, gridSize: int = 4):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.resizable(False, False)
        self.window.update()
        self.setup_ui(gridSize)

    def setup_ui(self,gridSize: int = 4):
        self.step_label = tk.Label(self.window, text="Step: 0", bg=BACKGROUND_COLOR, fg="white", font=FONT)
        self.step_label.pack(side=tk.TOP, fill=tk.X)
        self.score_label = tk.Label(self.window, text="Score: 0", bg=BACKGROUND_COLOR, fg="white", font=FONT)
        self.score_label.pack(side=tk.TOP, fill=tk.X)
        self.frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        self.frame.pack()
        self.cells = []
        for i in range(gridSize):
            row = []
            for j in range(gridSize):
                cell = tk.Label(self.frame, text="", bg=EMPTY_CELL_COLOR,
                                font=FONT, width=4, height=2)
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)

    def update_ui(self, game: Game2048, step: int = 0):
        self.step_label.config(text="Step: " + str(step))
        self.score_label.config(text="Score: " + str(game.score))
        for i in range(game.gridSize):
            for j in range(game.gridSize):
                value = game.grid[i][j]
                if value == 0:
                    self.cells[i][j].config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    self.cells[i][j].config(text=str(2**value), bg=CELL_COLORS.get(value, "#3c3a32"),
                                            fg=TEXT_COLORS.get(value, "white"))
        self.window.update_idletasks()
        self.window.update()