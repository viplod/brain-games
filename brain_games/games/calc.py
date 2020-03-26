import random


DESCRIPTION = "What is the result of the expression?"


def generate_round():
    operation_list = ['+', '-', '*']
    operation = random.choice(operation_list)
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = 'Question:, {} {} {}'.format(number1, operation, number2)
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    elif operation == '*':
        answer = number1 * number2
    return question, str(answer)
