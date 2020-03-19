import random
import prompt


def calc():
    for _ in range(0, 3):
        operation_list = ['+', '-', '*']
        operation = random.choice(operation_list)
        number1 = random.randint(0, 99)
        number2 = random.randint(0, 99)
        string = 'Question:, {} {} {}'.format(number1, operation, number2)
        print(string)
        answer = prompt.string('You answer: ')
        if operation == '+':
            if number1 + number2 == int(answer):
                print('Correct!')
            else:
                print(answer, ' is wrong answer ;(. Correct answer was ', str(number1 + number2))
                return False
        elif operation == '-':
            if number1 - number2 == int(answer):
                print('Correct!')
            else:
                print(answer, ' is wrong answer ;(. Correct answer was ', str(number1 - number2))
                return False
        elif operation == '*':
            if number1 * number2 == int(answer):
                print('Correct!')
            else:
                print(answer, ' is wrong answer ;(. Correct answer was ', str(number1 * number2))
                return False
        else:
            return False
    return True
