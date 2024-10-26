import requests

parameters = {
    "amount": 100,
    "type": "boolean",
}
api = "https://opentdb.com/api.php"

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
