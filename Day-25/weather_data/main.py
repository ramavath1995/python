import pandas

data = pandas.read_csv("weather_data.csv")
# print(data.temp.max())
# print(data.temp.min())
# print(data.temp.mean())

monday = data[data.day == "Monday"]
# print(monday)
# print(monday.condition)
# print(data[data.temp == data.temp.max()])


score_grading = {
    "names": ["Raju", "vishnu", "ravi", "krishna", "kumar"],
    "marks": [95, 88, 34, 62, 46,],
    "grading": ['Outstanding', 'Excellent', 'Fail', 'Good', 'Average']

}

data = pandas.DataFrame(score_grading)
data.to_csv("score_grading.csv")

print(data)
