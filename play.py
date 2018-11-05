import random


def get_computer_number():
    return computer

def get_human_data():
    return number

def print_results(computer, number):
    try:
        print('The computer has choosed:  ', computer)
        if number == computer:
            print('Draw!')
        elif (number == 1 and computer == 3) or\
            (number == 2 and computer == 1) or\
            (number == 3 and computer == 2):
            print('You win!!!')
        elif (number == 1 and computer == 2) or\
            (number == 2 and computer == 3) or\
            (number == 3 and computer == 1):
            print('You lost')
    except:
        TypeError


if __name__ == '__main__':
    print('Start the game: stone (1), paper (2) or scissors (3)')
    computer = random.randint(1, 3)
    number = int(input('Input: stone (1), paper (2) or scissors (3):  '))
    print_results(computer, number)
