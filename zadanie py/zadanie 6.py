def calculate_credit_hours(courses):
    total_credits = 0
    for course, credit in courses:
        total_credits += credit
    return total_credits

courses = [('Math', 3), ('History', 2)]
credits = calculate_credit_hours(courses)
print(credits)
