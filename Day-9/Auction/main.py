logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print("Welcome to Secret auction Program")

print(f"{logo}\n")
bidding_data = {}


def highest_bidder(bids):
    highest_bidder_name = ""
    highest_bidding_amount = 0
    for bidder in bids:
        amount = bids[bidder]
        if amount > highest_bidding_amount:
            highest_bidding_amount = amount
            highest_bidder_name = bidder
    print(f"The highest bidder is '{highest_bidder_name}' with bidding amount of Rs: {highest_bidding_amount}")


bidding_finished = False

while not bidding_finished:
    bidder_name = input("Enter bidder name: ").title()
    bidding_amount = float(input("What's bidding money? Rs: "))
    bidding_data[bidder_name] = bidding_amount
    more_bidders = input("Are there any bidders? type yes/no: ").lower()
    if more_bidders == "yes" or more_bidders == "y":
        pass
    else:
        highest_bidder(bidding_data)
        bidding_finished = True
