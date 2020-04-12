import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def get_answer():
    answer = prompt.string('You answer: ')
    return answer
