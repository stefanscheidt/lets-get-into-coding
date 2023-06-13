#! python3

from train_reservation_api import get_trains

print("Trains:")
for train in get_trains("http://localhost:8080"):
    print(f"> {train}")
