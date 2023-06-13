#! python3

import sys
from train_reservation_api import get_seats, post_reservation


if len(sys.argv) != 3:
    sys.stderr.write(f"Usage: {sys.argv[0]} <train_name> <seat_name>\n")
    sys.exit(1)

service_url = "http://localhost:8080"
train_name = sys.argv[1]
seat_name = sys.argv[2]
seats = get_seats(service_url, train_name)

if seat_name not in seats:
    sys.stderr.write(f"Train {train_name} does not have a seat {seat_name}\n")
    sys.exit(1)

seat = seats[seat_name]

if seat["booking_reference"] != "":
    sys.stderr.write(f"Seat {seat_name} is already reserved\n")
    sys.exit(1)

booking_reference = post_reservation(service_url, train_name, seat_name)
print(f"Successfully reserved seat {seat_name} on train {train_name}.")
print(f"Your booking reference is: {booking_reference}.")
