import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = f'{number1}, {number2}'
    answer = divisor(number1, number2)
    return question, str(answer)
