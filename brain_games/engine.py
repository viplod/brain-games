from brain_games.cli import get_name_user
from brain_games.cli import get_answer


COUNT_GAMES = 3


def run(game=None):
    print('Welcome to the Brain Games!')
    if not game:
        return
    print(game.DESCRIPTION)
    name = get_name_user()
    for _ in range(COUNT_GAMES):
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
