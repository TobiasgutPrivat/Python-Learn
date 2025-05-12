import os
import json
import time
from SudokuSolver.SudokuSolver import solveSudoku
import time
from SudokuAPI import fetch_and_cache_puzzles

save_dir = "runs"

class BenchmarkRun:
    puzzle: list[list[int]]
    solution: list[list[int]]
    time: float
    solved: list[list[int]]
    solvedCorrectly: bool

class Benchmark:
    runs: list[BenchmarkRun]
    difficulty: str
    num_puzzles: int

    def __init__(self, difficulty='medium', num_puzzles=10):
        self.difficulty = difficulty
        self.num_puzzles = num_puzzles
        self.runs = []

    def run(self):
        puzzles = fetch_and_cache_puzzles(self.difficulty, self.num_puzzles)

        for entry in puzzles:
            run = BenchmarkRun()
            self.runs.append(run)

            run.puzzle = entry["puzzle"]
            run.solution = entry["solution"]
            board = [row[:] for row in run.puzzle]

            start = time.time()
            run.solved = solveSudoku(board)
            end = time.time()
            run.time = end - start

            run.solvedCorrectly = run.solved == run.solution
            if run.solvedCorrectly:
                print("Solver failed to solve the puzzle.")
            else:
                print("Solver solved the puzzle correctly.")

    def save(self):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        folder = os.path.join(save_dir, self.difficulty)
        if not os.path.exists(folder):
            os.makedirs(folder)

        for i, run in enumerate(self.runs):
            filename = os.path.join(folder, f"run_{i}.json")
            with open(filename, "w") as f:
                json.dump(run.__dict__, f, indent=4)

    def printSummary(self):
        print(f"\nBenchmark Summary")
        print(f"Difficulty: {self.difficulty}")
        print(f"Total puzzles: {len(self.runs)}")
        print(f"Success rate: {sum(run.solvedCorrectly for run in self.runs) / len(self.runs) * 100:.2f}%")
        print(f"Average time: {sum(run.time for run in self.runs) / len(self.runs):.4f} seconds")

if __name__ == "__main__":
    benchmark = Benchmark(difficulty='hard', num_puzzles=5)
    benchmark.run()
    benchmark.printSummary()
    # benchmark.save()