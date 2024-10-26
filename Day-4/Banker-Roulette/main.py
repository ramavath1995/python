import random

peoples = input("Enter all the members name in your group separated by space: ").lower().split()

payer = random.choice(peoples)

print(f"{payer} will pay the bill today")
