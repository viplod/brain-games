import random
import prompt


def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False


def even():
	for _ in range(0,3):
		number = random.randint(0, 99)
		print('Question ', str(number))
		answer = prompt.string('You answer: ')
		if is_even(number) and answer == "yes":
			print('Correct!')
		elif not is_even(number) and answer == "no":
			print('Correct!')
		elif is_even(number):
			print("'no' is wrong answer ;(. Correct answer was 'yes'.")
			return False
		else:
			print("'yes' is wrong answer ;(. Correct answer was 'no'.")
			return False
	return True