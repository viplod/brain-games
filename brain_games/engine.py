def play_game(game = None):
	print('Welcome to the Brain Games!')
	if not game:
		return
	print(game.DESCRIPTION)
	name = get_name_user()