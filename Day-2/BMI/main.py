print("Welcome to BMI calculator")

height = float(input("What is your height in meters?: "))
weight = float(input("What is your weight in kg?: "))

bmi = weight / (height * height)

print(f"Your BMI is: {bmi}")
