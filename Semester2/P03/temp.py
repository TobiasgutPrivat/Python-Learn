import requests
import time

url = 'http://160.85.252.87/'

def evaluate_response(dict: dict[str,any]) -> None:
    filtered = {key: value for key, value in dict.items() if isinstance(value, int)}
    for key, value in filtered.items():
        print(f"{key:<15}","|", value)
    print("---------------+----------")
    print("SUM            |", sum(filtered.values()))

for i in range(10): # max: 2^10 = 1024s
    response = requests.get(url)
    if response.status_code == 200:
        decoded_data = response.json()
        corrected_data: dict[str,any] = {}
        for key in decoded_data.keys():
            corrected_key = key.encode('latin1').decode('utf-8')
            corrected_data[corrected_key] = decoded_data[key]
        evaluate_response(corrected_data)
        break
    
    time.sleep(1 * 2**i)