from random import randint
import math

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def isprime(n) -> bool:
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def clue(n):
    if isprime(n):
        print(color.PURPLE+'The Number Is A Prime'+color.END)
    else:
        print(color.PURPLE+'The Number Is Not A Prime'+color.END)

def clue2(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        print(color.PURPLE+'The Square Root Of The Number is An Integer'+color.END)
    else:
        print(color.PURPLE+'The Square Root Of The Number is not An Integer'+color.END)


s = 1

print(color.BLUE+f"\033[1mNUMBER GUESSING GAME\033[0m"+color.END+color.BLUE+'         '+'Author: Mahtab'+color.END)

while s == 1:
    user = 'a'

    while not user.isdigit():
        user = input('Enter The Range Till Which You Want To Guess The Number: ')
        if not user.isdigit():
            print(color.RED+'Invalid Number Or KeyWord..'+color.END)
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
            print(color.RED+"You've Entered Characters Or Wrong Keyword, You Need To Type Numbers Instead Of It"+color.END)
            print()
            us = input("Try Again: ")
            continue
        else:
            if int(us) > user:
                print(color.RED+"Sorry, Your Entered Number Was Not In The Range That You've Entered"+color.END)
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
                        attempt+=1
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
                    us = input(color.DARKCYAN+f"You Are Wrong, You Need To Guess {'Higher' if int(us) < target else 'Lower'}: "+color.END)
                    attempt += 1
                    print()

    s = input(color.GREEN+f"You've Guessed It Right In {attempt+1} attempts, Enter 1 If You Want To Play Again: "+color.END)

    if s == '1':
        s = 1