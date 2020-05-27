# URL Shortener - Python Project
from __future__ import with_statement
from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string

import contextlib
import sys

root = Tk()
root.geometry('400x200')
root.title("URL Shortener")
frame = Frame(root)

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def shorten():
    fullURL = entryURL.get()
    entryShort.delete(0, END)
    requestUrl = 'http://tinyurl.com/api-create.php?url='+fullURL
    with contextlib.closing(urlopen(requestUrl)) as response:
        entryShort.insert(0, response.read().decode('utf-8'))

def copyURL():
    temp = entryShort.get()
    pyperclip.copy(temp)

labelwelcome = Label(frame, text="URL Shortener", font=('Arial Bold', 12))
labelURL = Label(frame, text="Enter URL")
entryURL = Entry(frame)
labelShort = Label(frame, text="Shortened URL")
entryShort = Entry(frame)
generateBtn = Button(frame, text="Generate", command=shorten)
copyBtn = Button(frame, text="Copy", command=copyURL)
labelmsg = Label(root, text="Developed by Shahnawaz | Yashark", relief=SUNKEN)

frame.pack()
labelwelcome.grid(row=0, columnspan=2, pady=5)
labelURL.grid(row=1, sticky=E, pady=5)
entryURL.grid(row=1, column=1, ipadx=30, padx=5, pady=5, sticky=W)
labelShort.grid(row=2, sticky=E, pady=5)
entryShort.grid(row=2, column=1, ipadx=30, padx=5, pady=5, sticky=W)
generateBtn.grid(row=3)
copyBtn.grid(row=3, column=1, sticky=E)
labelmsg.pack(side=BOTTOM, fill=X, ipady=5)

root.mainloop()

