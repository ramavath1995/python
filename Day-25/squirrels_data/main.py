import pandas

data = pandas.read_csv("Squirrel_Data_2024.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

squirrels = {
    "color": ["gray", "red", "black"],
    "count": [gray, red, black]
}

squirrel_count = pandas.DataFrame(squirrels)
squirrel_count.to_csv("squirrel_count_2024.csv")
