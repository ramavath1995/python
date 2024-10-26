import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)
print("\nI'm thinking of a number between 1 to 100")

answer = random.randint(1, 100)

EASY_LEVEL_TURNS = 12
MODERATE_LEVEL_TURNS = 8
HARD_LEVEL_TURNS = 5

level = input("Select a level 'Easy', 'Moderate' or 'Hard': ").lower()


def choose_level(i):
    if i == "hard":
        return HARD_LEVEL_TURNS
    elif i == "moderate":
        return MODERATE_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def check_answer(a, g, t):
    if g == 0 or g > 100:
        print("Invalid guess\n")
    elif a > g:
        t -= 1
        print(f"Too low\n")
        return t
    elif a < g:
        t -= 1
        print(f"Too high\n")
        return t
    elif a == g:
        print(f"You got the answer {a}")


turns = choose_level(level)
game_finished = False
print(f"You have {turns} attempts to guess the answer")
while not game_finished:
    guess = int(input("Make a guess: "))
    turns = check_answer(answer, guess, turns)
    if turns == 0:
        print(f"Sorry out of attempts")
        game_finished = True
    elif answer == guess:
        game_finished = True
    else:
        print(f"You have {turns} attempts remaining to guess the answer")
