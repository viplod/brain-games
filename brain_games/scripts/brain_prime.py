from brain_games.cli import get_name_user
from brain_games.games.prime import prime


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def main():
    result = prime()
    if result:
        print('Congratulations,', name)
    else:
        print("Let's try again,", name, "!")


if __name__ == '__main__':
    main()
