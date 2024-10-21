def assignment_deadline(assignment_name, days_left):
    return f"Задание по {assignment_name} через {days_left} дней"

reminder = assignment_deadline('Python', 5)
print(reminder)
