import random
import operator


DESCRIPTION = "What is the result of the expression?"


def get_result_calculation(func, number1, number2):
    return func(number1, number2)


def generate_round():
    select_operation = random.choice(
        (
            ('+', operator.add),
            ('*', operator.mul),
            ('-', operator.sub),
        )
    )
    operation, func = select_operation
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = 'Question:, {} {} {}'.format(number1, operation, number2)
    answer = get_result_calculation(func, number1, number2)
    return question, str(answer)
