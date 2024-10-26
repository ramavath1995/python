print("Welcome to BMI calculator")

height = float(input("What is your height in meters?: "))
weight = float(input("What is your weight in kg?: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you're underweight")
elif 18.5 < bmi < 24.9:
    print(f"Your bmi is {bmi} and you're in the healthy weight")
elif 25 < bmi < 29.9:
    print(f"Your bmi is {bmi} and you're in the overweight")
elif 30 < bmi < 37.5:
    print(f"Your bmi is {bmi} and you're obese")
else:
    print(f"Your bmi is {bmi} and you're critically obese")
