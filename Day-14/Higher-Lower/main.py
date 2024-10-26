from data import data
import random
from art import *


def formatted_account(a):
    global country, name, description
    for i in a:
        name = a['name']
        country = a['country']
        description = a['description']
        return f"{name} is {description} from {country}"


def compare(a_f, b_f, g):
    if a_f > b_f and g == "a":
        return True
    elif a_f < b_f and g == "a":
        return False
    elif a_f > b_f and g == "b":
        return False
    elif a_f < b_f and g == "b":
        return True


print(logo)
score = 0
game_finished = False
account_a = random.choice(data)
account_b = random.choice(data)
while not game_finished:
    account_a = account_b
    while account_a == account_b:
        account_b = random.choice(data)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    print(f"\nA: {formatted_account(account_a)}")
    print(vs)
    print(f"\nB: {formatted_account(account_b)}")
    guess = input("Who has more followers A or B: ").lower()
    result = compare(a_followers, b_followers, guess)
    if result:

        score += 1
        if guess == "a":
            account_a = account_a
        else:
            account_a = account_b
        print(f"\nYou're right and your score is {score}")
    else:
        print(f"\nSorry that's wrong You're final score is {score}")
        game_finished = True
