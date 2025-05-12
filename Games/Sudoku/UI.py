import tkinter as tk

class SudokuSolverUI:
    def __init__(self, master, sudoku):
        self.master = master
        self.master.title("Sudoku Solver")
        self.master.geometry("600x600")

        self.sudoku = sudoku
        self.current_step = 0

        # Create a label to display the current step
        self.step_label = tk.Label(master, text=f"Step {self.current_step} of {len(self.sudoku.log)}")
        self.step_label.pack()

        # Create a frame to display the Sudoku board
        self.board_frame = tk.Frame(master)
        self.board_frame.pack()

        # Create labels to display the Sudoku board
        self.board_labels = []
        for row in range(9):
            row_labels = []
            for col in range(9):
                label = tk.Label(self.board_frame, text="", width=2, font=("Arial", 24))
                label.grid(row=row, column=col)
                row_labels.append(label)
            self.board_labels.append(row_labels)

        # Create a label to display the log step text
        self.log_step_label = tk.Label(master, text="", wraplength=500, font=("Arial", 14))
        self.log_step_label.pack()

        # Create buttons to navigate through the steps
        self.prev_button = tk.Button(master, text="Previous", command=self.prev_step)
        self.prev_button.pack()
        self.next_button = tk.Button(master, text="Next", command=self.next_step)
        self.next_button.pack()

        # Update the board display
        self.update_board_display()
        self.update_log_step_text()

    def update_board_display(self):
        for row in range(9):
            for col in range(9):
                cell = self.sudoku.log[self.current_step].board[row][col]
                if (col, row) in self.sudoku.log[self.current_step].markCause:
                    self.board_labels[row][col].config(text=str(cell or '-'), fg="white", bg="green")
                elif (col, row) in self.sudoku.log[self.current_step].markEffect:
                    self.board_labels[row][col].config(text=str(cell or '-'), fg="black", bg="yellow")
                else:
                    self.board_labels[row][col].config(text=str(cell or '-'), fg="black", bg="white")

    def update_log_step_text(self):
        self.log_step_label.config(text=self.sudoku.log[self.current_step].step)

    def prev_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.step_label.config(text=f"Step {self.current_step} of {len(self.sudoku.log)}")
            self.update_board_display()
            self.update_log_step_text()

    def next_step(self):
        if self.current_step < len(self.sudoku.log) - 1:
            self.current_step += 1
            self.step_label.config(text=f"Step {self.current_step} of {len(self.sudoku.log)}")
            self.update_board_display()
            self.update_log_step_text()