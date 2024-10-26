import random

names = ['Raju', 'Anil', 'Prasanth', 'Bhuvana', 'preetham', 'Dhakya', 'Kumar', 'vishnu', 'Ravi', 'Mohan']

students_scores = {student: random.randint(1, 99) for student in names}

print(students_scores)
passed_students = {key: value for (key, value) in students_scores.items() if value > 40}
print(passed_students)
