import random
import prompt


def divisor(val1, val2):
    maxdivisor = 1
    for index in range(1, val1 +1):
        if (val1 % index == 0) and (val2 % index == 0):
            maxdivisor = index
    return maxdivisor

def gcd():
    for _ in range(0, 3):
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        print('Question ', str(number1), str(number2))
        answer = prompt.integer('You answer: ')
        if number1 > number2:
            result = divisor(number2, number1)
        elif number1 < number2:
            result = divisor(number1, number2)
        else:
            result = number1        
        if answer == result:
            print('Correct!')
        else:
            print(answer, ' is wrong answer ;(. Correct answer was ', result)
            return False
    return True
