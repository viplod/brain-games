import random
from brain_games.cli import get_answer


def is_prime(number):
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


def prime():
    for _ in range(0, 3):
        number = random.randint(0, 99)
        print('Question ', str(number))
        answer = get_answer()
        if is_prime(number) and answer == "yes":
            print('Correct!')
        elif not is_prime(number) and answer == "no":
            print('Correct!')
        elif is_prime(number):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            return False
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return False
    return True
