from .Cell import Cell

class Step:
    board: list[list[Cell]] # deepcopied board
    step: str
    markCause: list[Cell]
    markEffect: list[Cell]

    def __init__(self, board: list[list[int]], step: str, markCause: list[tuple[int,int]] = [], markEffect: list[tuple[int,int]] = []):
        self.board = board
        self.step = step
        self.markCause = markCause
        self.markEffect = markEffect
    
    def print(self):
        print(f"Step: {self.step}")
        print("Board:")
        for row in self.board:
            print(['\033[97m' + (cell.getValue() or '-') + '\033[0m' if cell in self.markCause 
                else '\033[30m' + (cell.getValue() or '-') + '\033[0m' if cell in self.markEffect 
                else cell.getValue() or '-' for cell in row])