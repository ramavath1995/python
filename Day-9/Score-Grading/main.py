students_scores = {
    "Raju": 95,
    "vishnu": 88,
    "ravi": 34,
    "krishna": 62,
    "kumar": 46
}

score_grading = {}

for student in students_scores:
    score = students_scores[student]
    if score < 35:
        score_grading[student] = "Fail"
    elif score < 50:
        score_grading[student] = "Average"
    elif score < 65:
        score_grading[student] = "Good"
    elif score < 90:
        score_grading[student] = "Excellent"
    else:
        score_grading[student] = "Outstanding"

print(score_grading)