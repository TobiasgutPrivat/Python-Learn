import requests
import time
from SudokuSolver.SudokuSolver import solveSudoku
import os
import json
import time
import requests

CACHE_DIR = "cache"

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def get_cache_filename(difficulty, amount):
    return os.path.join(CACHE_DIR, f"{difficulty}_{amount}.json")

def fetch_and_cache_puzzles(difficulty='medium', amount=10):
    ensure_cache_dir()
    filename = get_cache_filename(difficulty, amount)

    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)

    puzzles = []
    for _ in range(amount):
        url = 'https://youdosudoku.com/api/'
        payload = {
            "difficulty": difficulty,
            "solution": True,
            "array": True
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            puzzle = [[int(i) for i in row] for row in data['puzzle']]
            solution = [[int(i) for i in row] for row in data['solution']]
            puzzles.append({
                "puzzle": puzzle,
                "solution": solution
            })
        else:
            raise Exception(f"Failed to fetch puzzle: {response.status_code}")

    with open(filename, "w") as f:
        json.dump(puzzles, f)

    return puzzles

def benchmark_solver(solver_function, difficulty='medium', num_puzzles=10):
    puzzles = fetch_and_cache_puzzles(difficulty, num_puzzles)
    times = []

    for entry in puzzles:
        puzzle = entry["puzzle"]
        board = [row[:] for row in puzzle]  # Copy to avoid mutation
        start = time.time()
        solved = solver_function(board)
        end = time.time()
        if not solved:
            print("Solver failed to solve the puzzle.")
        times.append(end - start)

    avg_time = sum(times) / len(times)
    print(f"{difficulty.capitalize()} puzzles average solve time: {avg_time:.4f} seconds")


if __name__ == "__main__":
    from Benchmark import benchmark_solver
    benchmark_solver(solveSudoku, difficulty='easy', num_puzzles=5)