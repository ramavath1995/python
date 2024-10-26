import requests
from datetime import datetime


TOKEN = "thenoobofalltime"
USER_NAME = "thenoob"
pixela_user_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_user_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_user_endpoint}/{USER_NAME}/graphs"

graph_header = {
    "X-USER-TOKEN": TOKEN,
}

graph_parameters = {
    "id": "graph1",
    "name": "Weight graph",
    "unit": "kilogram",
    "type": "float",
    "color": "momiji",
}

now = datetime.now()
today = now.strftime("%Y%m%d")

new_params = {
    "date": today,
    "quantity": "60",
}

response = requests.post(url=f"{graph_endpoint}/graph1", headers=graph_header, json=new_params)
print(response.text)
