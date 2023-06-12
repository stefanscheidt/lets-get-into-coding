#! python3

import requests

response = requests.get("http://127.0.0.1:8080/train-data/trains")

response.raise_for_status()

print("Trains:")
for train in response.json():
    print(f"- {train}")