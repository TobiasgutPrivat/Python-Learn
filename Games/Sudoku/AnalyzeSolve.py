from SudokuSolver.Sudoku import Sudoku
from SudokuAPI import get_puzzle
from UI import SudokuSolverUI
import tkinter as tk

def analyzeSudoku(difficulty: str, index: int) -> None:
    puzzle = get_puzzle(difficulty, index)["puzzle"]
    sudoku = Sudoku(len(puzzle), puzzle,True)
    sudoku.print()
    sudoku.solve()
    root = tk.Tk()
    my_gui = SudokuSolverUI(root, sudoku)
    root.mainloop()

if __name__ == "__main__":
    analyzeSudoku("easy", 0)