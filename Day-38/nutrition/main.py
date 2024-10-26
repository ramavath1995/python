import requests

API_KEY = "941994724ddafaaaff6cec314c2ff3ed"
APP_ID = "7d8aceb4"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

parameters = {
    "query": input("what did you done today: "),
    "gender": "male",
    "weight_kg": 55,
    "height_cm": 168,
    "age": 27
}

response = requests.post(nutrition_endpoint, headers=headers, params=parameters)
response.raise_for_status()
