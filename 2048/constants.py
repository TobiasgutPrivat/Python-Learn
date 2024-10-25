GRID_SIZE: int = 4
CELL_SIZE: int = 100
BACKGROUND_COLOR: str = "#bbada0"
EMPTY_CELL_COLOR: str = "#cdc1b4"
CELL_COLORS: dict[int, str] = {
    2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563",
    32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61",
    512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
}
TEXT_COLORS: dict[int, str] = {
    2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2",
    32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2",
    512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
}
FONT: tuple = ("Verdana", 24, "bold")