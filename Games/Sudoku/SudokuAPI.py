import os
import json
import requests

CACHE_DIR = "cache"

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def fetch_and_cache_puzzles(difficulty='medium', amount=10) -> list[dict]:
    ensure_cache_dir()
    difficultyFolder = os.path.join(CACHE_DIR, difficulty)

    sudokus: list[dict[list[list[int]]]] = []

    if not os.path.exists(difficultyFolder):
        os.makedirs(difficultyFolder)
    else:
        filenames = sorted([filename for filename in os.listdir(difficultyFolder) if filename.endswith(".json")], key=lambda x: int(x.split('.')[0]))
        for filename in filenames[:amount]:
            if filename.endswith(".json"):
                with open(os.path.join(difficultyFolder, filename), "r") as f:
                    sudokus.append(json.load(f))

    diffrence = amount - len(sudokus)

    if diffrence <= 0:
        return sudokus

    for _ in range(diffrence):
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
            sudokus.append({
                "puzzle": puzzle,
                "solution": solution
            })
        else:
            raise Exception(f"Failed to fetch puzzle: {response.status_code}")

    for i, sudoku in enumerate(sudokus):
        filename = os.path.join(difficultyFolder, f"{i}.json")
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump(sudoku, f, indent=4)

    return sudokus

def get_puzzle(difficulty='medium', index=10) -> list[dict]:
    filename = os.path.join(CACHE_DIR, difficulty, f"{index}.json")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        return fetch_and_cache_puzzles(difficulty, index+1)[index]