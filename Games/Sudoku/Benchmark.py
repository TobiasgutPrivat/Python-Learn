import requests
import time
from SudokuSolver.SudokuSolver import solveSudoku

def fetch_puzzle(difficulty='medium'):
    url = 'https://youdosudoku.com/api/'
    payload = {
        "difficulty": difficulty,
        "solution": True,
        "array": True
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['puzzle'], data['solution']
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def benchmark_solver(solver_function, difficulty='medium', num_puzzles=5):
    times = []
    for _ in range(num_puzzles):
        puzzle, solution = fetch_puzzle(difficulty)
        start_time = time.time()
        solved = solver_function([row[:] for row in puzzle])  # Deep copy to avoid mutation
        end_time = time.time()
        if not solved or solved != solution:
            print("Solver failed to solve the puzzle correctly.")
        else:
            print("Solver solved the puzzle correctly.")
        times.append(end_time - start_time)
    average_time = sum(times) / len(times)
    print(f"Average solving time for {difficulty} puzzles: {average_time:.4f} seconds")


if __name__ == "__main__":
    from Benchmark import benchmark_solver
    benchmark_solver(solveSudoku, difficulty='medium', num_puzzles=5)