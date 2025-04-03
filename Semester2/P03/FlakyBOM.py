import requests
import time

url = 'http://160.85.252.87/'

def evaluate_response(dict: dict[str,any]) -> None:
    filtered = {key: value for key, value in dict.items() if isinstance(value, int)}
    for key, value in filtered.items():
        print(f"{key:<15}","|", value)
    print("---------------+----------")
    print("SUM            |", sum(filtered.values()))
    #save to file
    with open("response.txt", "w") as f:
        for key, value in filtered.items():
            f.write(f"{key:<15} | {value}\n")
        f.write("---------------+----------\n")
        f.write(f"SUM            | {sum(filtered.values())}\n")

for i in range(10): # max: 2^10 = 1024s
    response = requests.get(url)
    if response.status_code == 200:
        evaluate_response(response.json())
        break
    
    time.sleep(1 * 2**i)