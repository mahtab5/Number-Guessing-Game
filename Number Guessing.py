from random import randint
import math


def isprime(n) -> bool:
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def clue(n):
    if isprime(n):
        print('The Number Is A Prime')
    else:
        print('The Number Is Not A Prime')


def clue2(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        print('The Square Root Of The Number is An Integer')
    else:
        print('The Square Root Of The Number is not An Integer')


s = 1

print(
    "NUMBER GUESSING GAME" + '         ' + 'Author: Mahtab')

while s == 1:
    user = 'a'

    while not user.isdigit():
        user = input('Enter The Range Till Which You Want To Guess The Number: ')
        if not user.isdigit():
            print('Invalid Number Or KeyWord..')
            print()

    if int(user) < 10:
        user = 10
        print('Your Entered Range Was Less Than 10, Setting It To 10 As Default....')
    print('Start Guessing The Number: ', end='\n')
    user = int(user)

    target = randint(1, user)
    wantclue = 0
    attempt = 0
    time = 0

    us = input()

    while us != str(target):

        if not us.isdigit() or not us:
            print(
                 "You've Entered Characters Or Wrong Keyword, You Need To Type Numbers Instead Of It")
            print()
            us = input("Try Again: ")
            continue
        else:
            if int(us) > user:
                print("Sorry, Your Entered Number Was Not In The Range That You've Entered")
                print()
                us = input("Try Again: ")
                continue
            else:
                if attempt == 3 and int(us) != target and wantclue != '1':
                    wantclue = input('Type 1 If You Want A Clue :')
                    if wantclue == '1':
                        clue(target)
                        print()
                        us = input("Try Again: ")
                        attempt += 1
                        continue
                    else:
                        wantclue = '1'
                        print()
                        us = input("Try Again: ")
                        continue

                elif attempt == 10 and int(us) != target and time != '1':
                    time = input('Type 1 If You Want Another Clue :')
                    if time == '1':
                        clue2(target)
                        us = input("Try Again: ")
                        attempt += 1
                        continue
                    else:
                        time = '1'
                        print()
                        us = input("Try Again: ")
                        continue

                if int(us) != target:
                    us = input(
                        f"You Are Wrong, You Need To Guess {'Higher' if int(us) < target else 'Lower'}: ")
                    attempt += 1
                    print()

    s = input(
        f"You've Guessed It Right In {attempt + 1} attempts, Enter 1 If You Want To Play Again: ")

    if s == '1':
        s = 1
