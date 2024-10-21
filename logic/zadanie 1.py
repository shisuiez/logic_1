def count_vowels_consonants(word):
    vowels = 'аеёиоуыэюя'
    consonants = 'бвгджзйклмнпрстфхцчшщ'

    vowels_count = 0
    consonants_count = 0

    word = word.lower()

    for letter in word:
        if letter in vowels:
            vowels_count += 1
        elif letter in consonants:
            consonants_count += 1

    return vowels_count, consonants_count


word = input("Введите слово: ")
vowels_count, consonants_count = count_vowels_consonants(word)

print(f'В слове "{word}" {vowels_count} гласные и {consonants_count} согласные буквы.')
