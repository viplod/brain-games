import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    index = random.randint(1, 9)
    step = random.randint(1, 10)
    start = random.randint(1, 99)
    progression = list(range(start, start + step * 10, step))
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, str(answer)
