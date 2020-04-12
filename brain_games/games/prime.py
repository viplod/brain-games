import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number


def generate_round():
    question = random.randint(1, 99)
    answer = is_prime(question)
    if is_prime(question):
        answer = "yes"
    else:
        answer = "no"
    return question, answer
