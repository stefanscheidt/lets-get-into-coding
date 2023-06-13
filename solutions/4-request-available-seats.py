#! python3

import sys
from train_reservation_api import get_seats 

def print_seats(p_train_name, p_seats):
    print(f"Available seats for train {p_train_name}:")
    for id, seat in p_seats.items():
        booking_reference = seat["booking_reference"]
        if booking_reference == "":
            status = "free"
        else:
            status = f"reserved ({booking_reference})"
        print(f"- {id}: {status}")


if len(sys.argv) != 2:
    sys.stderr.write(f"Usage: {sys.argv[0]} <train_name>\n")
    sys.exit(1)

train_name = sys.argv[1]
seats = get_seats("http://localhost:8080", train_name)
print_seats(train_name, seats)
