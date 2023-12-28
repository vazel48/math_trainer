import random


def generate_addition_question(level):
    if level == "1":
        min_val, max_val = 3, 30
    elif level == "2":
        min_val, max_val = 11, 100
    else:
        min_val, max_val = 21, 1000

    a = random.randint(min_val, max_val)
    b = random.randint(min_val, max_val)

    question = f"{a} + {b}"
    correct_result = a + b

    return question, correct_result
