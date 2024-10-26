print("Welcome to Tip calculator\n")

bill = float(input("What is the total bill?: "))

tip_percent = int(input("How much percent tip do want to give 5 or 8 or 10?: "))
tip = bill * tip_percent / 100

total = bill + tip

print(f"Your total bill is {total}")
