import random

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
             "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


print("\nWelcome to Password Generator\n")

no_letters = int(input("How many letters do you want in your password?: "))
no_symbols = int(input("How many symbols do you want in your password?: "))
no_numbers = int(input("How many numbers do you want in your password?: "))

password_list = []

for letter in range(no_letters):
    new_letter = random.choice(alphabets)
    password_list += new_letter
for symbol in range(no_symbols):
    new_symbol = random.choice(symbols)
    password_list += new_symbol
for number in range(no_numbers):
    new_number = random.choice(numbers)
    password_list += new_number

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(password)
