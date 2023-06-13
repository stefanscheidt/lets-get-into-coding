import requests, sys


def get_booking_reference(service_url):
    response = requests.post(f"{service_url}/booking-reference")
    response.raise_for_status()
    return response.text


def get_trains(service_url):
    response = requests.get(f"{service_url}/train-data/trains")
    response.raise_for_status()
    return response.json()


def get_seats(service_url, train_name):
    get_train_response = requests.get(f"{service_url}/train-data/trains/{train_name}")
    if get_train_response.status_code == 404:
        sys.stderr.write(f"Train {train_name} is unknown.\n")
        sys.exit(1)
    get_train_response.raise_for_status()

    return  get_train_response.json()["seats"]


def post_reservation(service_url, train_name, seat_name):
    booking_reference = get_booking_reference(service_url)
    payload = {"train_id": train_name, "seats": [seat_name], "booking_reference": booking_reference}
    response = requests.post(f"{service_url}/train-data/reserve", json = payload)
    response.raise_for_status()
    return booking_reference
