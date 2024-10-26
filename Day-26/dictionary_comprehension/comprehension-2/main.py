w_in_c = eval(input("Enter day and its celsius temperature: "))
# The Eval function evaluates the string expression and returns its value. For example, Eval("1 + 1") returns 2.
result = {day: (c*9/5)+32 for (day, c) in w_in_c.items()}
print(result)


# input={'monday': 11, 'tuesday': 12, 'wednesday': 14, 'thursday': 16, 'friday': 15, 'saturday': 13}
