from brain_games.cli import welcome_user
from brain_games.games.calc import calc


def main():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = welcome_user()
    result = calc()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()