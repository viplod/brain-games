from brain_games.scripts.brain_games import main
from brain_games.cli import welcome_user
from brain_games.even import even




def brain_even():
	main()
	print('Answer "yes" if number even otherwise answer "no".')
	name = welcome_user()
	result = even()
	if result:
		print('Congratulations,', name)
	else:
		print("Let's try again,", name ,"!")


