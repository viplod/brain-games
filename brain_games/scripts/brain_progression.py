from brain_games.cli import get_name_user
from brain_games.games.progression import progression


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = get_name_user()
    result = progression()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
