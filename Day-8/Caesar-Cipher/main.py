alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v",
             "w", "x", "y", "z"]


def caesar_cipher(t, s, d):
    final_message = ""
    for i in t:
        if i not in alphabets:
            final_message += i
        else:
            n = alphabets.index(i)
            if d == "encrypt" or d == "encode":
                new_shift = n + s
            else:
                new_shift = n - s
            new_letter = alphabets[new_shift]
            final_message += new_letter
    return final_message


direction = input("What do you want 'encode' or 'decode'? type encrypt for encode or decrypt for decode: ").lower()
text = input("Write your message: ").lower()
shift = int(input("How many shifts do you want?: "))

shift_amount = shift % 26
if direction == "encrypt" or direction == "encode":
    print(f"Your {direction}ed text is '{caesar_cipher(text, shift_amount, direction)}'")
elif direction == "decrypt" or direction == "decode":
    print(f"Your {direction}ed text is '{caesar_cipher(text, shift_amount, direction)}'")
else:
    print("Please select correct direction")
