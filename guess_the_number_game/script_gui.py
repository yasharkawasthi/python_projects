from tkinter import *
from tkinter.ttk import *
import random as rm
import string

root = Tk()
root.geometry('400x200')
root.title("Guess the Number")
frame = Frame(root)

num = rm.randint(0, 100)
chances = 4
flag = 0


def checkNumber():
    try:
        while chances > 0:
            try:
                n = entryPass.get("1.0", 'end-1c')
            except ValueError:
                labelGuess.insert(
                    10, "Sorry,this is not a numerical value , try again :( ")
                continue
            if n == num:
                print("You have guessed the number.")
                flag = 1
                break
            elif n > 100 or n < 0:
                print("Invalid")
            elif n-num > 10:
                print("Too high")
            elif num-n > 10:
                print("Too low")
            elif abs(n-num) >= 5:
                print("Nearby")
            elif abs(n-num) < 5:
                print("You're very close!")
                chances -= 1
                n = int(input("Guess again = "))

    except KeyboardInterrupt:
        if flag == 1:
            print("Congratulations, you won! You guessed it with",
                  chances, "chances left.")
        else:
            print("You lost.")


labelwelcome = Label(frame, text="Make your guess", font=('Arial Bold', 12))
labelPass = Label(frame, text="Your Guess")
entryPass = Entry(frame)
generateBtn = Button(frame, text="Check", command=checkNumber)
labelGuess = Label(frame, text="", font=('Arial', 10))
labelmsg = Label(root, text="Developed by Shahnawaz & Yashark", relief=SUNKEN)

frame.pack()
labelwelcome.grid(row=0, columnspan=2, pady=5)
labelPass.grid(row=1, sticky=E, pady=5)
entryPass.grid(row=1, column=1, ipadx=13, padx=5, pady=5, sticky=W)
generateBtn.grid(row=2, columnspan=2, pady=5)
labelGuess.grid(row=3, columnspan=2, pady=5)
labelmsg.pack(side=BOTTOM, fill=X, ipady=5)


root.mainloop()
