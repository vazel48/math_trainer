import random


def multiplication_quiz():
    print("Вітаємо у тренажері таблиці множення!")

    level = input("Оберіть рівень складності: Звичайний школяр (1) / Ентузіаст (2) / Математик-маньяк (3): ")

    if level == "1":
        min_val, max_val = 2, 10
    elif level == "2":
        min_val, max_val = 3, 12
    else:
        min_val, max_val = 6, 15

    correct_answers = 0

    for question_num in range(1, 16):
        a = random.randint(min_val, max_val)
        b = random.randint(min_val, max_val)
        correct_result = a * b

        user_answer = int(input(f"{question_num} приклад: {a} * {b} = "))

        if user_answer == correct_result:
            print(random.choice(["Вірно!", "Молодець!", "Super!", "Чудово!"]))
            correct_answers += 1
        else:
            print(f"Помилився, правильна відповідь: {correct_result}.")

    print(f"\nГра закінчена. Ви правильно відповіли на {correct_answers} з 15 запитань!\nТак тримати!")

    play_again = input("Хочете зіграти ще раз? (yes/no): ")
    if play_again.lower() == 'yes':
        multiplication_quiz()

# Запуск програми
multiplication_quiz()
