import prompt


def get_name_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name

def get_answer():
	answer = prompt.string('You answer: ')	
	return answer

