def find_countries_by_colors():

    flags = {
        'ru': ['red', 'blue', 'white'],         # Россия
        'uk': ['blue', 'yellow'],               # Украина
        'it': ['green', 'white', 'red'],        # Италия
        'fr': ['blue', 'white', 'red'],         # Франция
        'de': ['black', 'red', 'yellow'],       # Германия
        'kr': ['white', 'blue', 'red', 'black'],# Южная Корея
        'kg': ['red', 'yellow'],                # Кыргызстан
        'kz': ['blue', 'yellow'],               # Казахстан
        'us': ['red', 'white', 'blue'],         # Сша
        'jp': ['white', 'red'],                 # Япония
        'cn': ['red', 'yellow'],                # Китай
        'br': ['green', 'yellow', 'blue'],      # Бразилия
        'in': ['orange', 'white', 'green', 'blue'], # Индия
        'za': ['green', 'yellow', 'black', 'white', 'red', 'blue'] # Южная Африка
    }


    colors = input("Введите цвет: ").lower().split()


    result = [domain for domain, flag_colors in flags.items() if all(color in flag_colors for color in colors)]


    if result:
        print("Страны с этими цветами в флаге:", result)
    else:
        print("Нет такого цвета")


find_countries_by_colors()
