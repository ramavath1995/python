print("Welcome to Spicy pizza\n")

profit = 0
print("prices\nSmall-150, Medium-200, Large-300\n")
size = input("Select a size 'Small', 'Medium', 'Large': ").lower()
if size == "small":
    profit += 150
    cheese = input("Do you want extra cheese? type yes/no: ").lower()
    if cheese == "y" or cheese == "yes":
        profit += 30
    pepperoni = input("Do you want extra pepperoni? type yes/no: ").lower()
    if pepperoni == "y" or pepperoni == "yes":
        profit += 20
    pay = float(input(f"please pay Rs: {profit} "))
    if pay >= profit:
        change = abs(profit - pay)
        print(f"Your order is confirmed\nHere your change: {change}")
    else:
        print("Sorry not enough money")
elif size == "medium":
    profit += 200
    cheese = input("Do you want extra cheese? type yes/no: ").lower()
    if cheese == "y" or cheese == "yes":
        profit += 30
    pepperoni = input("Do you want extra pepperoni? type yes/no: ").lower()
    if pepperoni == "y" or pepperoni == "yes":
        profit += 20
    pay = float(input(f"please pay Rs: {profit} "))
    if pay >= profit:
        change = abs(profit - pay)
        print(f"Your order is confirmed\nHere your change: {change}")
    else:
        print("Sorry not enough money")
elif size == "large":
    profit += 300
    cheese = input("Do you want extra cheese? type yes/no: ").lower()
    if cheese == "y" or cheese == "yes":
        pass
    pepperoni = input("Do you want extra pepperoni? type yes/no: ").lower()
    if pepperoni == "y" or pepperoni == "yes":
        pass
    pay = float(input(f"please pay Rs: {profit} "))
    if pay >= profit:
        change = abs(profit - pay)
        print(f"Your order is confirmed\nHere your change: {change}")
    else:
        print("Sorry not enough money")

