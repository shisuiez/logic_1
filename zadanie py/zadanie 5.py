def next_class_schedule(current_day):
    schedule = {
        'Monday': ' Новый год',
        'Tuesday': ' День защитника Отечества',
        'Wednesday': 'Международный женский день',
        'Thursday': 'Нооруз',
        'Friday': ' День Победы'
    }
    return schedule.get(current_day, "No class")

next_class = next_class_schedule('Monday')
print(next_class)
