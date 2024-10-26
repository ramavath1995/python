my_input = input("Write a sentence here: ").split()

result = {word: len(word) for word in my_input}

print(result)
