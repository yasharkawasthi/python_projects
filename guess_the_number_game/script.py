# Guess The Number Game - Python Project

import random as rm

num = rm.randint(0, 100)
chances = 4
flag = 0

# Adding exceptional handling feature to prevent the program from terminating if input value is non numeric
try:
    while chances > 0:
        try:
            n = int(input('Enter your guess: '))
        except ValueError:
            print("Sorry,this is not a numerical value , try again :( ")
            continue
        if n == num:
            print("You have guessed the number.")
            flag = 1
            break
        elif n > 100 or n < 0:
            print("Invalid")
        elif n-num > 10:
            print("Too high! Make a lower guess")
        elif num-n > 10:
            print("Too low! Make a higher guess")
        elif abs(n-num) >= 5:
            print("Nearby")
        elif abs(n-num) < 5:
            print("You're very close!")
            chances -= 1
            n = int(input("Guess again = "))

except KeyWordInterrupt:
    if flag == 1:
        print("Congratulations, you won! You guessed it with",
              chances, "chances left.")
    else:
        print("You lost.")
