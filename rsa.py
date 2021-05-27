from tkinter import *
from tkinter import ttk
import math
from binascii import hexlify, unhexlify
import random



# ------------GUI--------
# main screen
master = Tk()
master.title('RSA DIGITAL SIGNATURE')
option = StringVar()
mode1 = StringVar()
k = StringVar()

# first field:
Label(master, text="Pirmas laukas", font=(
    "Arial", 15)).grid(row=2, sticky=W, padx=5)
FirstEntry = Entry(master)
FirstEntry.grid(row=2, column=1)

# button generate signature
button1 = Button(master, text='generuoti', width=8)
button1.grid(row=3, column=1)

# second:
Label(master, text="Antras laukas", font=(
    "Arial", 15)).grid(row=4, sticky=W, padx=5)
SecondEntry = Entry(master)
SecondEntry.grid(row=4, column=1)

# button modify
button2 = Button(master, text='modifikuoti', width=8 )
button2.grid(row=5, column=1)

# third:
Label(master, text="Trecias laukas", font=(
    "Arial", 15)).grid(row=6, sticky=W, padx=5)
ThirdEntry = Entry(master)
ThirdEntry.grid(row=6, column=1)

# button to get result
button3 = Button(master, text='patvirtinti', width=8 )
button3.grid(row=7, column=1)


# field for result:
Label(master, text="Rezultatas", font=(
    "Arial", 15)).grid(row=10, sticky=W, padx=5)
ResultEntry = Entry(master)
ResultEntry.grid(row=10, column=1)


# size of the page
master.geometry('400x400')
master.mainloop()
