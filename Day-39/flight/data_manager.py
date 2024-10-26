import requests

SHETTY_API = "https://api.sheety.co/22bf20c4cc69092801bc63b0c4b0bf95/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        r = requests.get(SHETTY_API)
        data = r.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            r = requests.put(f"{SHETTY_API}/{city['id']}", json=new_data)
            print(r.text)
