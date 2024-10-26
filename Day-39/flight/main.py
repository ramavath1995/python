from data_manager import DataManager
from flight_search import FlightSearch

api_key = "KdmoEWeK1_ozPR-BGBoIAUIQP1wzr_gU"
affilid = "dhakyaflightsearch"

data_manager = DataManager()
shetty_data = data_manager.get_destination_data()
if shetty_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in shetty_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(shetty_data)

        data_manager.destination_data = shetty_data
        data_manager.update_destination_code()
