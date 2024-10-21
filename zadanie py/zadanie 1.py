def average(*args):
    return sum(args) / len(args)

def calculate_gpa(*grades):
    return average(*grades)

print(calculate_gpa(3.0, 3.5, 4.0, 4.5))
