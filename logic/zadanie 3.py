import random


def choose_word():
    words = ['python', 'apple', 'banana', 'orange', 'computer']
    return random.choice(words)


def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Добро пожаловать в игру 'Угадай слово'!")

    while attempts > 0:
        print(f"\nТекущее слово: {display_word(word, guessed_letters)}")
        print(f"Осталось попыток: {attempts}")
        guess = input("Угадай букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Пожалуйста, введи одну букву.")
            continue

        if guess in guessed_letters:
            print(f"Ты уже угадал букву '{guess}'.")
        elif guess in word:
            print(f"Отлично! Буква '{guess}' есть в слове.")
            guessed_letters.add(guess)
        else:
            print(f"Нет, буквы '{guess}' нет в слове.")
            attempts -= 1
            guessed_letters.add(guess)

        if all(letter in guessed_letters for letter in word):
            print(f"\nПоздравляю! Ты угадал слово: {word}")
            break
    else:
        print(f"\nТы проиграл! Загаданное слово было: {word}")


if __name__ == "__main__":
    play_game()
