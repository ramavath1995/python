fruits = eval(input("enter fruits names: "))

# allows us to evaluate the Python expression as a 'string' and return the value as an integer


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(f'{fruit} pie')


make_pie(4)

# sample input
# ['apple', 'banana', 'mango', 'grapes']
