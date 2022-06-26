import random

def random_number_guess():
    print('RANDOM NUMBER GAME - BETWEEN 0 AND 10')
    r = random.randrange(0, 10)
    ipt = input('Please enter your number guess: ')
    if ipt == r:
        print(str(r) + " correct")
    elif ipt != r:
        print('Incorrect')
        random_number_guess()
random_number_guess()