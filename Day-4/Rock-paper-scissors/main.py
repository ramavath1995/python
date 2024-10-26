import random

rock = '''
"Rock= "
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

"Paper= "
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
"Scissors= "
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choice = random.randint(0, 2)
answer = [rock, paper, scissors]
print("0 for Rock, 1 for Paper, 2 for Scissors\n")

user_choice = int(input("Type 0, 1, or 2: "))

if user_choice > 2 or user_choice < 0:
    print("Sorry select correct option")
else:
    if user_choice == computer_choice:
        print(f"It's Draw, computer also choose {answer[computer_choice]}")
    elif computer_choice == 2 and user_choice == 0:
        print(f"You Win computer choose {answer[computer_choice]}")
    elif computer_choice == 0 and user_choice == 2:
        print(f"You loose computer choose {answer[computer_choice]}")
    elif computer_choice > user_choice:
        print(f"You loose computer choose {answer[computer_choice]}")
    elif computer_choice < user_choice:
        print(f"You Win computer choose {answer[computer_choice]}")
