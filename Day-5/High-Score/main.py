students_score = input("Enter students score separated by space: ").split()

high_score = 0
for score in students_score:
    int_score = int(score)
    if int_score > high_score:
        high_score = int_score
print(f"High score is {high_score}")
