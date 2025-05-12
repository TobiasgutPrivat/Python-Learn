from .Cell import Cell

class Step:
    board: list[list[int]] # deepcopied board
    step: str
    markCause: list[tuple[int,int]]
    markEffect: list[tuple[int,int]]
    
    def __init__(self, board: list[list[int]], step: str, markCause: list[tuple[int,int]] = [], markEffect: list[tuple[int,int]] = []):
        self.board = board
        self.step = step
        self.markCause = markCause
        self.markEffect = markEffect
    
    def print(self):
        print(f"Step: {self.step}")
        print("Board:")
        height = len(self.board)
        width = len(self.board[0])
        for row in range(height):
            # print([str(self.board[row][col] or '-') for col in range(width)])
            print(['\033[97m' + str(self.board[row][col] or '-') + '\033[0m' if (col, row) in self.markCause 
                else '\033[30m' + str(self.board[row][col] or '-') + '\033[0m' if (col, row) in self.markEffect 
                else str(self.board[row][col] or '-') for col in range(width)])
