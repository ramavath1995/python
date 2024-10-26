import requests

api_key = "KdmoEWeK1_ozPR-BGBoIAUIQP1wzr_gU"
search_api_endpoint = "https://api.tequila.kiwi.com/locations/query"

class FlightSearch:

    def get_destination_code(self, city_name):
        header = {
            "apikey": api_key,
        }

        parameters = {
            "term": city_name,
            "location_types": "city",
        }
        r = requests.get(url=f"{search_api_endpoint}", headers=header, params=parameters)
        r.raise_for_status()
        response = r.json()["locations"]
        code = response[0]["code"]
        print(code)
        return code
