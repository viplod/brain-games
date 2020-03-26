import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def divisor(val1, val2):
    maxdivisor = 1
    for index in range(1, val1 + 1):
        if (val1 % index == 0) and (val2 % index == 0):
            maxdivisor = index
    return maxdivisor


def generate_round():
    number1 = random.randint(1, 99)
    number2 = random.randint(1, 99)
    question = f'{number1}, {number2}'
    if number1 > number2:
        answer = divisor(number2, number1)
    elif number1 < number2:
        answer = divisor(number1, number2)
    else:
        answer = number1
    return question, str(answer)
