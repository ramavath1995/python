import random
from art import *

words_list = ['bluesky', 'panther', 'psycho', 'chemistry', 'ocean', 'thunder', 'therapy', 'birthday', 'president',
              'apartment', 'cradle', 'coffee', 'trampoline', 'waterfall', 'window', 'proud', 'flashlight', 'marry',
              'judge', 'shadow', 'measure', 'guitar', 'drums', 'basketball', 'baseball', 'football',
              'archery', 'subway', 'azure', 'pixel', 'bikini', 'cycle', 'zombie', 'bike', 'train', 'ugly'
              'hockey', 'monkey', 'elephant', 'rabbit', 'shark', 'snake', 'whale', 'cinderella', 'frozen', 'bounce',
              'giggle', 'scissors', 'golf', 'chicken', 'sneeze', 'chimpanzee', 'hammer', 'clap', 'happy', 'spoon',
              'cough', 'oxygen', 'puppy', 'vodka', 'wiskey', 'gossip', 'stretch', 'motor'
              'drink', 'penguin', 'toothbrush', 'phone', 'umbrella', 'duck', 'photographer']


def hang_man():
    word = random.choice(words_list)
    answer = ""

    for i in word:
        answer += i

    empty_word = []

    for char in range(0, len(word)):
        empty_word += "_"

    turns = 7

    print(f"The word has {len(word)} letters {empty_word} and you have {turns} attempts to guess a word\n")
    game_on = False

    while not game_on:
        guess = input("Guess a letter: ").lower()

        if guess in empty_word:
            print(f"You already guessed letter '{guess}'\n")

        for position in range(len(word)):
            letter = word[position]
            if letter == guess:
                empty_word[position] = letter

        if guess not in empty_word:
            turns -= 1
            print(stages[turns])
            print(f"Sorry letter {guess} not in word \nYou have {turns} attempts left to guess a word")
            if turns == 0:
                print(f"\nSorry out of attempts")
                game_on = True
        print(f"{empty_word}\n")
        if "_" not in empty_word:
            print(f"Congrats you guessed the word '{answer}'")

            game_on = True


hang_man()
repeat = input("Do you want to play again?: ").lower()
if repeat == "y" or repeat == "yes":
    hang_man()
