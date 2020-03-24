from brain_games.cli import get_name_user
from brain_games.games.calc import calc

DESCRIPTION = "What is the result of the expression?"


def main():
    result = calc()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
