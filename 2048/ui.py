import tkinter as tk
from game import Game2048
from constants import GRID_SIZE, CELL_SIZE, BACKGROUND_COLOR, EMPTY_CELL_COLOR, CELL_COLORS, TEXT_COLORS, FONT

class GameUI:
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
        self.frame = tk.Frame(self.window, bg=BACKGROUND_COLOR)
        self.frame.grid()
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
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                value = self.game.grid[i][j]
                if value == 0:
                    self.cells[i][j].config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    self.cells[i][j].config(text=str(value), bg=CELL_COLORS.get(value, "#3c3a32"),
                                            fg=TEXT_COLORS.get(value, "white"))

    def key_handler(self, event):
        new_grid = None
        if event.keysym == 'Up':
            new_grid = self.game.move_up()
        elif event.keysym == 'Down':
            new_grid = self.game.move_down()
        elif event.keysym == 'Left':
            new_grid = self.game.move_left()
        elif event.keysym == 'Right':
            new_grid = self.game.move_right()

        if new_grid is not None:
            self.game.update_grid(new_grid)
            self.update_ui()

            if not self.game.can_move():
                self.end_game()

    def end_game(self):
        self.frame.destroy()
        end_label = tk.Label(self.window, text="Game Over!", bg=BACKGROUND_COLOR, fg="white", font=FONT)
        end_label.pack()