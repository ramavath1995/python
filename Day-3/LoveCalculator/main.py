print("Welcome to Love Calculator")

f_name = input("What is your name?: ").lower()
s_name = input("What is others name?: ").lower()

c_name = f_name + s_name

t = c_name.count("t")
r = c_name.count("r")
u = c_name.count("u")
e = c_name.count("e")

true = t + r + u + e

l = c_name.count("l")
o = c_name.count("o")
v = c_name.count("v")
e = c_name.count("e")

love = l + o + v + e

true_love = str(true) + str(love)
score = int(true_love)

if score < 10 or score > 90:
    print(f"Your love score is '{score}'. You both like coke and mentos")
elif score < 30 or score > 60:
    print(f"Your love score is '{score}'. You both normal together")
else:
    print(f"Your love score is '{score}'. You both perfect together")
