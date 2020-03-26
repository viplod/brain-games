import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def generate_round():
    question = random.randint(1, 99)
    answer = is_prime(question)
    if is_prime(question):
        answer = "yes"
    else:
        answer = "no"
    return question, answer
