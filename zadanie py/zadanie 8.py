def scholarship_eligibility(average_grade):
    if average_grade >= 4.5:
        return True
    else:
        return False

print(scholarship_eligibility(4.6))
print(scholarship_eligibility(4.4))
