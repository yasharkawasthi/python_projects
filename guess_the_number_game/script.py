# Guess The Number Game - Python Project

import random as rm

num = rm.randint(0, 100)
chances = 4
flag = 0

n = int(input("Guess the randomly generated number = "))
while chances > 0:
    if n == num:
        print("You have guessed the number.")
        flag = 1
        break
    elif n > 100 or n < 0:
        print("Invalid")
    elif n-num > 10:
        print("The number you guessed is too high. Make a lower guess")
    elif num-n > 10:
        print("The number you guessed is too low. Make a higher guess")
    elif abs(n-num) >= 5:
        print("You're close!")
    elif abs(n-num) < 5:
        print("You're almost there!")
    chances -= 1
    n = int(input("Guess again = "))

if flag == 1:
    print("Congratulations, you won! You guessed it with",
          chances, "chances left.")
else:
    print("You lost.")
