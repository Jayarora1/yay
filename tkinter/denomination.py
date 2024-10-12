from tkinter import *
from tkinter import messagebox
from PIL import image,imageTk

w = Tk()
w.title("Denominations calculator")
w.configure(bg= "yellow")
w.geometry("500x500")
def topwin():
    top = Toplevel()
    top.title("Denomoninations calculator")
    top.geometry("500x500+50+50")

    label = Label(top, text= "Please enter the total amount", bg= "light grey")
    e = Entry(top)
    lbl = Label(top, text = "here are the total number of notes",bg= "light grey")

    l1 = Label(top, text=100)
    l2 = Label(top, text=500)
    l3 = Label(top, text=1000)

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(e.get())
            note2000 = amount // 2000
            note2000 %= amount
            note500 = amount // 500
            note500 %= amount
            note100 = amount // 100
            
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note100))
        except ValueError:
            print("There is an error please put an actual number")

    btn = Button(top,text = "Calculate",command=calculator,bg="pink",fg = "green")
