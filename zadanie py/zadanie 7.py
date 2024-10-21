def get_highest_score(students_scores):
    max_score = -1
    top_student = ''
    for student, score in students_scores.items():
        if score > max_score:
            max_score = score
            top_student = student
    return top_student

students_scores = {'Саня': 85, 'вася': 90, 'Эржан': 78}
top_student = get_highest_score(students_scores)
print(top_student)
