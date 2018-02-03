from tkinter import *
from tkinter import messagebox
import os
import sys


root = Tk()

bclick = True
k = 0
i = 0

# prebacivanje poteza i glavni dio igre odrađen ovdje :D :D

def potez(buttons):
    global i
    global k
    global bclick

    if buttons["text"] == "-" and bclick == True:
        buttons["text"] = "X"
        bclick = False

    elif buttons["text"] == "-" and bclick == False:
        buttons["text"] = "O"
        bclick = True

    if bt1["text"] == "X" and bt2["text"] == "X" and bt3["text"] == "X":

        messagebox.showinfo("čestitamo ", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt4["text"] == "X" and bt5["text"] == "X" and bt6["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        (k) = k+1
        print(k)
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")

    if bt7["text"] == "X" and bt8["text"] == "X" and bt9["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt1["text"] == "X" and bt4["text"] == "X" and bt7["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt2["text"] == "X" and bt5["text"] == "X" and bt8["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt3["text"] == "X" and bt6["text"] == "X" and bt9["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt3["text"] == "X" and bt5["text"] == "X" and bt7["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt1["text"] == "X" and bt5["text"] == "X" and bt9["text"] == "X":
        messagebox.showinfo("čestitamo", "pobjednik je X")
        k = k + 1
        l3.config(text=k)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt1["text"] == "O" and bt2["text"] == "O" and bt3["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt4["text"] == "O" and bt5["text"] == "O" and bt6["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt7["text"] == "O" and bt8["text"] == "O" and bt9["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt1["text"] == "O" and bt4["text"] == "O" and bt7["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt2["text"] == "O" and bt5["text"] == "O" and bt8["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt3["text"] == "O" and bt6["text"] == "O" and bt9["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt3["text"] == "O" and bt5["text"] == "O" and bt7["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")
    if bt1["text"] == "O" and bt5["text"] == "O" and bt9["text"] == "O":
        messagebox.showinfo("čestitamo", "pobjednik je O")
        i = i + 1
        l4.config(text=i)
        bt1.config(state="disabled")
        bt2.config(state="disabled")
        bt3.config(state="disabled")
        bt4.config(state="disabled")
        bt5.config(state="disabled")
        bt6.config(state="disabled")
        bt7.config(state="disabled")
        bt8.config(state="disabled")
        bt9.config(state="disabled")

    return i, k






buttons = StringVar()

#definiranje labela, gumbova za glavni prvo prozor

l1 = Label(root, text="pobjede X :")
l2 = Label(root, text="pobjede O :")
l3 = Label(root, text=k)
l4 = Label(root, text=i)



newGame = Button(root, text="New game", height=3, width=8, fg="red", bg="green", command=lambda: new_game())
reset = Button(root, text="Reset", height=3, width=8, fg="red", bg="blue", state="disabled", command=lambda: reset_game())
bt1 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt1))
bt2 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt2))
bt3 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt3))
bt4 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt4))
bt5 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt5))
bt6 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt6))
bt7 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt7))
bt8 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt8))
bt9 = Button(root, text="-", height=4, width=8, state="disabled", command=lambda: potez(bt9))

# na pritisak tipke new game otvara se novi prozor sa upisivanjem imena igrača
def new_game():
    bt1["text"] = "-"
    bt2["text"] = "-"
    bt3["text"] = "-"
    bt4["text"] = "-"
    bt5["text"] = "-"
    bt6["text"] = "-"
    bt7["text"] = "-"
    bt8["text"] = "-"
    bt9["text"] = "-"
    bt1.config(state="active")
    bt2.config(state="active")
    bt3.config(state="active")
    bt4.config(state="active")
    bt5.config(state="active")
    bt6.config(state="active")
    bt7.config(state="active")
    bt8.config(state="active")
    bt9.config(state="active")
    l3.config(text=0)
    l4.config(text=0)

    prozor = Tk()
    l5 = Label(prozor, text="Prvi igrač: ")
    l6 = Label(prozor, text="Drugi igrač: ")
    e1 = Entry(prozor)
    s1=e1.get()
    e2 = Entry(prozor)
    s2=e2.get()
    unesi=Button(prozor, text="Unesi", height=3, width=8, fg="red", bg="green", command=lambda:unos())
    l5.grid(row=0, column=0, sticky="W")
    l6.grid(row=1, column=0, sticky="W")
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    unesi.grid(row=2, column=0)

    newGame.config(state="disabled")
    bt1.config(state="disabled")
    bt2.config(state="disabled")
    bt3.config(state="disabled")
    bt4.config(state="disabled")
    bt5.config(state="disabled")
    bt6.config(state="disabled")
    bt7.config(state="disabled")
    bt8.config(state="disabled")
    bt9.config(state="disabled")
    reset.config(state="disabled")

    def unos():
        l1.config(text=s1)
        l2.config(text=s2)
        bt1.config(state="active")
        bt2.config(state="active")
        bt3.config(state="active")
        bt4.config(state="active")
        bt5.config(state="active")
        bt6.config(state="active")
        bt7.config(state="active")
        bt8.config(state="active")
        bt9.config(state="active")
        reset.config(state="active")
        newGame.config(state="active")
        prozor.destroy()

# funkcija za resetiranje igre postavlja sve na početni naziv
def reset_game():
     bt1["text"] = "-"
     bt2["text"] = "-"
     bt3["text"] = "-"
     bt4["text"] = "-"
     bt5["text"] = "-"
     bt6["text"] = "-"
     bt7["text"] = "-"
     bt8["text"] = "-"
     bt9["text"] = "-"
     bt1.config(state="active")
     bt2.config(state="active")
     bt3.config(state="active")
     bt4.config(state="active")
     bt5.config(state="active")
     bt6.config(state="active")
     bt7.config(state="active")
     bt8.config(state="active")
     bt9.config(state="active")


#postavljanje labela i gumbica u grid

var = StringVar()

newGame.grid(row=3, column=2)
reset.grid(row=3, column=0)
bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
bt3.grid(row=0, column=2)
bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=2, column=0)
bt8.grid(row=2, column=1)
bt9.grid(row=2, column=2)
l1.grid(row=4, column=0, sticky="W")
l2.grid(row=5, column=0, sticky="W")
l3.grid(row=4, column=1, sticky="W")
l4.grid(row=5, column=1, sticky="W")






root.mainloop()