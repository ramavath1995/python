height = float(input("Enter height of wall: "))
width = float(input("Enter width of wall: "))


def calc(h, w, c):
    no_of_cans = h * w / c

    return no_of_cans


coverage = 5
print(f"You need {calc(height, width, coverage)} liters of paint")
