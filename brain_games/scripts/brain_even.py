from brain_games.cli import get_name_user
from brain_games.games.even import even

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'

def main():
    result = even()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
