# Random Password Generator - Python Project

import random

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','`','~','-','_','=','+','[','{',']','}','\\','|',';',':','\'','"',',','<','.','>','/','?']

allChars = digits + lowers + uppers + symbols

oneDigit = random.choice(digits)
oneLower = random.choice(lowers)
oneUpper = random.choice(uppers)
oneSymbol = random.choice(symbols)

password = oneDigit+oneLower+oneUpper+oneSymbol

print ("Random Password Generator")
print ("Minimum Characters = 5\nMaximum Characters = 20")

length = int(input("Enter Number of Characters you want in Password = "))

if length<5:
    length=5
elif length>20:
    length=20

for c in range(length-4):
    password=password+random.choice(allChars)

print ("Random Password Generated Just For You = "+password)

