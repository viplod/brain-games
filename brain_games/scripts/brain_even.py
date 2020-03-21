from brain_games.cli import welcome_user
from brain_games.games.even import even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = welcome_user()
    result = even()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
