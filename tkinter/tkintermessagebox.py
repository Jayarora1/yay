from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Messagebox")
root.geometry('400x400')

def msg():
    messagebox.showinfo("You have a virus scanning the file")
button = Button(root, text = 'click me im not virus',command=msg,bg="yellow")
button.place(x=50,y=50)
root.mainloop()
