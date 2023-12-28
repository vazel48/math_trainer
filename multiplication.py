import random


def generate_multiplication_question(level):
    if level == "1":
        min_val, max_val = 2, 9
    elif level == "2":
        min_val, max_val = 3, 12
    else:
        min_val, max_val = 5, 16

    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)

    question = f"{a} * {b}"
    correct_result = a * b

    return question, correct_result

