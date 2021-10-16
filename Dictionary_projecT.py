from tkinter import *
from PyDictionary import PyDictionary

#creating objects
dictionary=PyDictionary()
root=Tk()

#set geometry
root.geometry("500x500")
def dict():
    meaning.config(text=dictionary.meaning(word.get()))
    synonym.config(text=dictionary.synonym(word.get()))
    antonym.config(text=dictionary.antonym(word.get()))

#adding labels ,buttons and frames
Label(root,text="DICTIONARY",font=("Helvetica 29 bold"),fg="blue").pack(pady=10)

#frame 1
frame=Frame(root)
Label(frame,text="Type Spelling...",font=("Helvetica 29 bold")).pack(side=LEFT)
word=Entry(frame,font=("Helvetica 25 bold"))
word.pack()
frame.pack(pady=10)

#frame 2
frame1=Frame(root)
Label(frame1,text="Meaning :) ",font=("Helvetica 10 bold")).pack(side=LEFT)
meaning=Label(frame1,text="",font=("Helvetica 10"))
meaning.pack()
frame1.pack(pady=10)

#frame 3
frame2=Frame(root)
Label(frame2,text="Synonym :) ",font=("Helvetica 10 bold")).pack(side=LEFT)
synonym=Label(frame2,text="",font=("Helvetica 10"))
synonym.pack()
frame2.pack(pady=10)

#frame 4
frame3=Frame(root)
Label(frame3,text="Antonym :) " ,font=("Helvetica 10 bold")).pack(side=LEFT)
antonym=Label(frame3,text="",font=("Helvetica 10"))
antonym.pack(side=LEFT)
frame3.pack(pady=10)
Button(root,text="SEARCH..",font=("Helvetica 15 bold"),command=dict).pack()

root.mainloop()

