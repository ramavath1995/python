logo = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

print(logo)

print("Welcome to Treasure-Map hunt")

road = input("You're across the road type 'left' or 'right': ").lower()
if road == "left":
    print("You reached at the river.")
    island = input("Their is a island in the river type 'wait' or 'swim': ").lower()
    if island == "wait":
        print("You reached the island\nTheir are four rooms namely 'green', 'blue', 'red', and 'yellow'")
        room = input("Out of 4 rooms one room has treasure, choose correct room: ").lower()
        if room == "yellow":
            print("Yeah hooooo you find the treasure room 🏆🏆🏆🏆🏆🏆🏆🏆")
        elif room == "red":
            print("Sorry room filled with fire 🔥")
        elif room == "green":
            print("Sorry room filled with snake 🐍")
        elif room == "blue":
            print("Sorry room filled with lions 🦁")
    else:
        print("Sorry long shark attacked on you 🐬")
else:
    print("Sorry a huge truck crushed you 😱")
