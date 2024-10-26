
row1 = ["󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜"]
row2 = ["󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜"]
row3 = ["󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜", "󠀠󠀠󠀠󠀠󠀠󠁝⬜"]

treasure_map = [row1, row2, row3]

choice = input("You're treasure hidden in 'X'. Where do you want to place the treasure?: ")

a = ["a", "b", "c"]
letter_index = a.index(choice[0].lower())
number_index = int(choice[1]) - 1

treasure_map[number_index][letter_index] = "X"
print(f"{row1}\n{row2}\n{row3}")
