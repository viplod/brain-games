from brain_games.cli import welcome_user
from brain_games.games.progression import progression


def main():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = welcome_user()
    result = progression()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
