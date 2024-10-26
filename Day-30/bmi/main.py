h = float(input("Height in meter?: "))
w = float(input("Weight in kg: "))

if h > 3:
    raise ValueError("Human height should not over 3 meters")

bmi = w / h ** 2
print(f"Your bmi is {bmi}")
