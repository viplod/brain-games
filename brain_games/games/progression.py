import random
import prompt


def progression():
    for _ in range(0, 3):
        index = random.randint(1, 9)
        step = random.randint(1, 10)
        start = random.randint(1, 99)
        progression = list(range(start, start + step * 10, step))
        result = progression[index]
        progression[index] = '..'
        print('Question ', str(progression))
        answer = prompt.integer('You answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(answer, ' is wrong answer ;(. Correct answer was ', result)
            return False
    return True
