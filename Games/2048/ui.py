import tkinter as tk
from game import Game2048
from constants import GRID_SIZE, BACKGROUND_COLOR, EMPTY_CELL_COLOR, CELL_COLORS, TEXT_COLORS, FONT

class GameUI:
    game: Game2048
    window: tk.Tk
    score_label: tk.Label
    frame: tk.Frame
    cells: list[list]
    def __init__(self):
        self.game = Game2048()
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.resizable(False, False)
        self.setup_ui()
        self.update_ui()

        self.window.bind("<Key>", self.key_handler)
        self.window.mainloop()

    def setup_ui(self):
        self.score_label = tk.Label(self.window, text="Score: 0", bg=BACKGROUND_COLOR, fg="white", font=FONT)
        self.score_label.pack(side=tk.TOP, fill=tk.X)
        self.frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        self.frame.pack()
        self.cells = []
        for i in range(GRID_SIZE):
            row = []
            for j in range(GRID_SIZE):
                cell = tk.Label(self.frame, text="", bg=EMPTY_CELL_COLOR,
                                font=FONT, width=4, height=2)
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)

    def update_ui(self):
        self.score_label.config(text="Score: " + str(self.game.score))
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.game.grid[i][j]
                if value == 0:
                    self.cells[i][j].config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    self.cells[i][j].config(text=str(2**value), bg=CELL_COLORS.get(value, "#3c3a32"),
                                            fg=TEXT_COLORS.get(value, "white"))

    def key_handler(self, event: tk.Event):
        if event.keysym == 'Up':
            self.game.move(0)
        elif event.keysym == 'Down':
            self.game.move(1)
        elif event.keysym == 'Left':
            self.game.move(2)
        elif event.keysym == 'Right':
            self.game.move(3)

        self.update_ui()

        if self.game.is_game_over:
            self.end_game()

    def end_game(self):
        self.frame.destroy()
        end_label = tk.Label(self.window, text="Game Over!", bg=BACKGROUND_COLOR, fg="white", font=FONT)
        end_label.pack()