import random


def generate_subtraction_question(level):
    if level == "1":
        min_val, max_val = 3, 30
    elif level == "2":
        min_val, max_val = 9, 100
    else:
        min_val, max_val = 11, 1000

    # Generate and sort in reverse order to avoid negative numbers in the answer
    a, b = sorted([random.randint(min_val, max_val), random.randint(min_val, max_val)], reverse=True)

    question = f"{a} - {b}"
    correct_result = a - b

    return question, correct_result
