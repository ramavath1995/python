import pandas

data = pandas.read_csv("nato.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Enter a word: ").upper()

result = [phonetic_dict[letter] for letter in name]
print(result)
