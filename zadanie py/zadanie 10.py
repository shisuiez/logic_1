def calculate_library_fine(days_late):
    fine_per_day = 5
    total_fine = days_late * fine_per_day
    return total_fine

fine = calculate_library_fine(3)
print(fine)
