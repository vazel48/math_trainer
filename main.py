import random
from variables import calc

num_of_questions = 12
print(calc)
print("Вітаю у тренажері таблиці множення!")
print(f"Пропоную вирішити {num_of_questions} прикладів.")


def multiplication_quiz():
    level = input("Обери рівень складності: Звичайний школяр (1) / Ентузіаст (2) / Математик-маніяк (3): ")

    if level == "1":
        min_val, max_val = 2, 9
    elif level == "2":
        min_val, max_val = 3, 12
    else:
        min_val, max_val = 5, 15

    correct_answers = 0
    used_questions = set()
    question_num = 0

    while question_num < num_of_questions:
        a, b = random.randint(min_val, max_val), random.randint(min_val, max_val)

        if (a, b) not in used_questions:
            used_questions.add((a, b))
            correct_result = a * b
            user_answer = int(input(f"{question_num + 1} приклад: {a} * {b} = "))

            if user_answer == correct_result:
                print(random.choice(["Вірно!", "Чемпіон!", "Молодець!", "Давай ще!", "Так тримати!",
                                     "Супер!", "Чудово!", "Супер-пупер!", "Красунчик!", "Правильно!"]))
                correct_answers += 1
            else:
                print(f"Будь уважним, правильна відповідь: {correct_result}.")

            question_num += 1

    print(f"\nРаунд закінчився! Ти правильно відповів на {correct_answers} з {num_of_questions} запитань!")

    play_again = input("Хочеш зіграти ще раз? (yes/no): ")
    if play_again.lower() == 'yes':
        multiplication_quiz()


# Запуск програми
multiplication_quiz()
