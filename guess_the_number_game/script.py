# Guess The Number Game - Python Project

import random as rm

num = rm.randint(0,100)
#print(num)
chances = 4
flag = 0

n = int(input("Guess the randomly generated number = "))
while chances>0:
    if n==num:
        print ("You guessed the number.")
        flag=1
        break
    elif n>100 or n<0:
        print ("Invalid")
    elif n-num>10:
        print ("Too high")
    elif num-n>10:
        print ("Too low")
    elif abs(n-num)>=5:
        print ("Nearby")
    elif abs(n-num)<5:
        print("You're too close!")
    chances-=1
    n = int(input("Guess again = "))

if flag==1:
    print("Congratulations, you won! You guessed it with",chances,"chances left.")
else:
    print("You lost.")
