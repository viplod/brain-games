from brain_games.cli import welcome_user
from brain_games.games.gcd import gcd


def main():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    name = welcome_user()
    result = gcd()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
