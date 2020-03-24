from brain_games.cli import get_name_user
from brain_games.games.progression import progression


DESCRIPTION = 'What number is missing in the progression?'

def main():
    result = progression()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
