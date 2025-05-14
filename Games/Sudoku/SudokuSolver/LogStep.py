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
