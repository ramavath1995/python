import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 11, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def declare_winner(user, computer):
    if user == computer:
        return f"It's Draw"
    elif user == 0:
        return f"You Win"
    elif computer == 0:
        return f"You Lose"
    elif user > 21:
        return f"You Lose you went over 21"
    elif computer > 21:
        return f"You Win computer went over 21"
    elif computer > user:
        return f"You lose"
    else:
        return f"You win"


game_finished = False
computer_cards = [deal_card() for i in range(2)]
user_cards = [deal_card() for j in range(2)]
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(logo)
while not game_finished:
    print(f"\nYour first cards are {user_cards} and your score is {user_score}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_finished = True
    else:
        another_card = input("Do you want to draw another card?: ").lower()
        if another_card == "yes" or another_card == "y":
            user_cards.append(deal_card())
            user_score = sum(user_cards)
        else:
            game_finished = True
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
print(f"Your final cards are {user_cards} and your final score {user_score}")
print(f"Computer final cards are {computer_cards} and your final score {computer_score}")
print(declare_winner(user_score, computer_score))
