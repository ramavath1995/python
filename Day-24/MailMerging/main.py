PLACER_HOLDER = "[name]"

with open("./Input/Names/names.txt") as file:
    names_list = file.readlines()


with open("Input/Letters/starting_letter.txt", 'r') as file:
    content = file.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = content.replace(PLACER_HOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as my_letter:
            my_letter.write(new_letter)