import pandas

data = pandas.read_csv("nato.csv")

dict_data = {row.letter: row.code for (index, row) in data.iterrows()}
output = None


def phanatic_word():
    global output
    word = input("Enter a word: ").upper()
    try:
        output = [dict_data[i] for i in word]
    except KeyError:
        print("sorry only alphabets are allowed")
        phanatic_word()
    finally:
        print(output)


phanatic_word()
