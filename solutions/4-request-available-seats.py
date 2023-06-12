#! python3

import sys, requests

if len(sys.argv) != 2:
    sys.stderr.write(f"Usage: {sys.argv[0]} <train_name>\n")
    sys.exit(1)

train_name = sys.argv[1]
get_train_response = requests.get(f"http://127.0.0.1:8080/train-data/trains/{train_name}")
if get_train_response.status_code == 404:
    sys.stderr.write(f"Train {train_name} is unknown.\n")
    sys.exit(1)
get_train_response.raise_for_status()

seats = get_train_response.json()["seats"]
print(f"Available seats for train {train_name}:")
for id, seat in seats.items():
    booking_reference = seat["booking_reference"]
    if booking_reference == "":
        status = "free"
    else:
        status = f"reserved ({booking_reference})"
    print(f"- {id}: {status}")
