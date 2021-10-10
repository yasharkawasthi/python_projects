from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string

root = Tk()
root.geometry('400x200')
root.title("Random Password Generator")
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


labelwelcome = Label(
    frame, text="Random Password Generator", font=('Arial Bold', 12))
labelPass = Label(frame, text="Password")
labelLen = Label(frame, text="Length")
entryPass = Entry(frame)
generateBtn = Button(frame, text="Generate Password", command=generatePass)
copyBtn = Button(frame, text="Copy Password", command=copypass)
labelmsg = Label(root, text="Developed by M. Shahnawaz Alam", relief=SUNKEN)
combo = Combobox(frame, textvariable=lengthSelect)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
combo.current(0)
combo.bind('<<ComboboxSelected>>')

frame.pack()
labelwelcome.grid(row=0, columnspan=2, pady=5)
labelPass.grid(row=1, sticky=E, pady=5)
entryPass.grid(row=1, column=1, ipadx=13, padx=5, pady=5, sticky=W)
labelLen.grid(row=2, sticky=E, pady=5)
combo.grid(row=2, column=1, sticky=W, padx=5, ipadx=4)
generateBtn.grid(row=3)
copyBtn.grid(row=3, column=1, sticky=E)
labelmsg.pack(side=BOTTOM, fill=X, ipady=5)


root.mainloop()
