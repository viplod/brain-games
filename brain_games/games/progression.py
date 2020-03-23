import random
from brain_games.cli import get_answer


def progression():
    for _ in range(0, 3):
        index = random.randint(1, 9)
        step = random.randint(1, 10)
        start = random.randint(1, 99)
        progression = list(range(start, start + step * 10, step))
        result = progression[index]
        progression[index] = '..'
        print('Question ', str(progression))
        answer = get_answer()
        if int(answer) == result:
            print('Correct!')
        else:
            print(answer, ' is wrong answer ;(. Correct answer was ', result)
            return False
    return True
