# Speed Typing Test - Python Project
from time import time
from tkinter import *

root = Tk()
root.geometry('800x600')
root.title("Speed Typing Test")
frame = Frame(root)

given_text = "Rutters Plate Fleet boom chandler Brethren of the Coast handsomely lookout marooned brigantine knave. Buccaneer gangway jack rum loot spyglass line Jack Tar fore gaff. Gaff topmast scuttle ballast swab draught measured fer yer chains dance the hempen jig Chain Shot yardarm."

def start():
    global start_time
    start_time = time()

def end():
    end_time = time()
    time_taken = end_time - start_time
    final_time = round(time_taken,2)
    typed_text = entrySubmitText.get("1.0", "end")
    words = typed_text.split()
    wordlen = len(words)
    res = wordlen / (time_taken / 60)
    speed = round(res,2)
    given_words = given_text.split()
    givenwordlen = len(given_words)
    errors = abs(givenwordlen - wordlen)
    
    for i in range(len(given_words)):
        if words[i] == given_words[i]:
            continue
        else:
            errors += 1
            
    text = "You took "+str(final_time)+" seconds with an Average Speed of "+str(speed)+" words per minute with "+str(errors)+" errors."
    entryResult.insert("1.0",text)

labeltop = Label(frame, text="Type the following text", font=('Arial Bold', 12))
entryGivenText = Text(frame, width=60, height=10)
entrySubmitText = Text(frame, width=60, height=10)
entryResult = Text(frame, width=60, height=2)

frame.pack()
labeltop.grid(row=0, columnspan=3)
entryGivenText.grid(row=1)
entryGivenText.insert(1.0, given_text)
entryGivenText.configure(state='disabled')
startBtn = Button(frame, text="Start", command=start)
submitBtn = Button(frame, text="Submit", command=end)
startBtn.grid(row=2, padx=20)
entrySubmitText.grid(row=3, pady=10)
submitBtn.grid(row=4, padx=20)
entryResult.grid(row=5, pady=20)

root.mainloop()
