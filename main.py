import random
from variables import calc
from addition import generate_addition_question
from subtraction import generate_subtraction_question
from multiplication import generate_multiplication_question

num_of_questions = 12

print(calc)
print("Вітаю у математичному тренажері!")
print(f"Пропоную вирішити {num_of_questions} прикладів. Час необмежений.")
# Номерація прикладів where?


def get_operation_choice():
    print("Обери дію: Додавання (1) / Віднімання (2) / Множення (3) / Random (4)")
    return input("Твій вибір: ")


def get_level():
    return input("Обери рівень складності: Першокласник (1) / Master_Raven (2) / Heihachi_Mishima (3): ")


def quiz():
    operation = get_operation_choice()
    level = get_level()

    correct_answers = 0
    question_number = 1

    for _ in range(num_of_questions):
        if operation == "1" or (operation == "4" and random.choice(["1", "2", "3"]) == "1"):
            question, correct_result = generate_addition_question(level)  # tuple unpacking
        elif operation == "2" or (operation == "4" and random.choice(["1", "2", "3"]) == "2"):
            question, correct_result = generate_subtraction_question(level)  # tuple unpacking
        else:
            question, correct_result = generate_multiplication_question(level)  # tuple unpacking

        try:
            user_answer = int(input(f"{question_number} приклад: {question} = "))
            if user_answer == correct_result:
                print(random.choice(["Вірно!", "Чемпіон!", "Молодець!", "Давай ще!", "Так тримати!",
                                     "Супер!", "Чудово!", "Супер-пупер!", "Красунчик!", "Правильно!"]))
                correct_answers += 1
            else:
                print(f"Будь уважнішим, правильна відповідь: {correct_result}.")
        except ValueError:
            print("Це не схоже на число. Будь уважнішим!")
        question_number += 1

    print(f"\nРаунд закінчився! Ти правильно вирішив {correct_answers} з {num_of_questions} прикладів!")

    # Обрахунок відсотка правильних відповідей
    percentage_correct = (correct_answers / num_of_questions) * 100
    # Визначення рівня успішності на основі відсотка
    if percentage_correct == 100:
        print("Відмінно!")
    elif percentage_correct >= 70:
        print("Молодець!")
    else:
        print("Трішки піднажми!")

    play_again = input("\nХочеш зіграти ще раз? (yes/no): ")
    if play_again.lower() == 'yes':
        quiz()


quiz()
