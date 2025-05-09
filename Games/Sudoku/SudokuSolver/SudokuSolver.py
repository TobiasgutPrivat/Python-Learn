from .Sudoku import Sudoku

def solveSudoku(sudoku:list[list[int]]) -> list[list[int]]:
    '''
    Solve a sudoku puzzle using the Sudoku class.
    '''
    print("Solving Sudoku...")
    sudokuSolver = Sudoku(len(sudoku),sudoku)
    sudokuSolver.print()
    sudokuSolver.solve()
    print("Solved Sudoku:")
    sudokuSolver.print()
    sudoku = sudokuSolver.getList()
    return sudoku