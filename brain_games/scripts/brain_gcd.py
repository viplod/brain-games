from brain_games.cli import get_name_user
from brain_games.games.gcd import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    result = gcd()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
