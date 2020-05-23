# Dice Rolling Simulator - Python Project

import random as rm

choice = True

while choice:
    num = rm.randint(1,6)
    print("Dice rolled and got",num)
    c = input("Do you want to roll the dice again. (Y/N) = ")
    if c=='N' or c=='n':
        choice = False

