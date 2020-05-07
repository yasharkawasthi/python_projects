#Speed Typing Test - Python Project
from time import time
from tkinter import *

global start_time
start_time = time()
root = Tk()
root.geometry('800x600')
root.title("Speed Typing Test")
frame = Frame(root)
entryResult = Text(frame, width=60, height=4)
def typingSpeed(typed_text, start_time):
    global time
    global words
    global speed
    end_time = time()
    time_taken = end_time - start_time
    time = round(time_taken, 2)
    words = typed_text.split()
    wordLen = len(words)
    res = wordLen / (time / 60)
    entryResult.insert(2.0, res)

def typingErrors(given_text):
        global given_words
        given_words = given_text.split()
        errors = 0
        for i in range(len(words)):
                if words[i]==given_words[i]:
                        continue
                else:
                        errors+=1
        return errors


given_text="Rutters Plate Fleet boom chandler Brethren of the Coast handsomely lookout marooned brigantine knave. Buccaneer gangway jack rum loot spyglass line Jack Tar fore gaff. Gaff topmast scuttle ballast swab draught measured fer yer chains dance the hempen jig Chain Shot yardarm."

labeltop = Label(frame, text="Type the following text", font=('Arial Bold', 12))
entryGivenText = Text(frame, width=60, height=10)
entrySubmitText = Text(frame, width=60, height=10)
typed_text = entrySubmitText.get("1.0", "end")
submitBtn = Button(frame, text="Submit", command=typingSpeed(typed_text, start_time))


frame.pack()
labeltop.grid(row=0, columnspan=3)
entryGivenText.grid(row=1)
entryGivenText.insert(1.0, given_text)
entryGivenText.configure(state='disabled')
entrySubmitText.grid(row=2, pady=10)
submitBtn.grid(row=3, padx=20)
entryResult.grid(row=4, pady=15)


#errors = typingErrors(given_text)

#print("You took",time,"seconds with an Average Speed of",speed,"words per minute with",errors,"errors.")
root.mainloop()