from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string

root = Tk()
root.geometry('400x200')
root.title("Guess the Number")
frame = Frame(root)

lengthSelect = IntVar()
choice = IntVar()


def strong():
    entryPass.delete(0, END)
    length = lengthSelect.get()
    password = string.ascii_letters + string.digits + "!@#$&*"
    return ''.join((random.choice(password) for i in range(length)))


def generatePass():
    generatedPass = strong()
    entryPass.insert(10, generatedPass)


def copypass():
    temp = entryPass.get()
    pyperclip.copy(temp)


labelwelcome = Label(frame, text="Make your guess", font=('Arial Bold', 12))
labelPass = Label(frame, text="Your Guess")
entryPass = Entry(frame)
generateBtn = Button(frame, text="Check", command=generatePass)
labelGuess = Label(frame, text="asdnjknjk", font=('Arial', 10))
labelmsg = Label(root, text="Developed by Shahnawaz & Yashark", relief=SUNKEN)

frame.pack()
labelwelcome.grid(row=0, columnspan=2, pady=5)
labelPass.grid(row=1, sticky=E, pady=5)
entryPass.grid(row=1, column=1, ipadx=13, padx=5, pady=5, sticky=W)
generateBtn.grid(row=2, columnspan=2, pady=5)
labelGuess.grid(row=3, columnspan=2, pady=5)
labelmsg.pack(side=BOTTOM, fill=X, ipady=5)


root.mainloop()
