from SudokuSolver.Sudoku import Sudoku
from SudokuAPI import get_puzzle

def analyzeSudoku(difficulty: str, index: int) -> None:
    puzzle = get_puzzle(difficulty, index)["puzzle"]
    sudoku = Sudoku(len(puzzle), puzzle,True)
    sudoku.print()
    sudoku.solve()
    for i in range(len(sudoku.log)):
        print(f"Step {i}:")
        sudoku.log[i].print()
        if input("Continue ... ").lower() == "exit":
            break

if __name__ == "__main__":
    analyzeSudoku("easy", 0)