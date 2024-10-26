import csv

with open("weather_data.csv") as data:
    content = data.readlines()
# print(content)


with open("weather_data.csv") as data:
    data_file = csv.reader(data)
    temperature = []
    for row in data_file:
        temp = row[1]
        if temp != "temp":
            temperature.append(int(temp))
print(temperature)
