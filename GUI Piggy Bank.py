balance=0
lt=0

from tkinter import *

root=Tk()
f=Frame(root)
db=Button(f,text="Deposit")
wb=Button(f,text="Withdraw")
c=Button(root,text="Clear")
e=Entry(root)
show=Text(root)
s=Button(root,text="Print Statement")

balance=0
lt=0
def deposit(amount):
    global balance
    global lt
    amount=int(e.get())
    if (amount>0):
        balance= (balance+amount)
        lt=(amount)   
    show.insert(END,"{}\n".format("Deposited"))

def withdraw(amount):
    global balance
    global lt
    amount=int(e.get())
    if (balance>=amount):
        balance=balance-amount
        lt=-amount
    show.insert(END,"{}\n".format("Withdraw"))

def clear (amount):
    e.delete(0,END)
    show.delete(1.0,"end")

def statement(amount):
    global balance
    global lt
    show.insert(END,"{}\n".format("This is Your balance"))
    show.insert(END,"{}\n".format(balance))
    show.insert(END,"{}\n".format("This is Your Last Transaction"))
    show.insert(END,"{}\n".format(lt))

e.pack(side="top")
show.pack(side='top')
f.pack(side="top")
db.pack(side="left")
wb.pack(side="left")
s.pack(side="top")
c.pack(side="top")


db.bind("<Button>",deposit)
wb.bind("<Button>",withdraw)
s.bind("<Button>",statement)
c.bind("<Button>",clear)

root.mainloop()