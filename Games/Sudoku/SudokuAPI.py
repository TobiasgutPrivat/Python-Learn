import os
import json
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