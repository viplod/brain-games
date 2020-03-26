import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = random.randint(1, 99)
    if is_even(question):
        answer = "yes"
    else:
        answer = "no"
    return question, answer
