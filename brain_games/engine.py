from brain_games.cli import get_user_name
from brain_games.cli import get_answer


NUMBER_OF_GAMES = 3


def run(game=None):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = get_user_name()
    for _ in range(NUMBER_OF_GAMES):
        question, answer = game.generate_round()
        print(f'Question , {question}')
        user_answer = get_answer()
        if user_answer != answer:
            print(f'{user_answer} is wrong answer ;(., correct answer '
                  f'{answer}.')
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
