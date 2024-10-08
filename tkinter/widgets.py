from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry('400x400')
root.title("Image")

upload = Image.open('abc.jpg' )
Image1 = ImageTk.PhotoImage(upload)

label = Label(root,image=Image1,height=200,width=200)
label.place(x=40,y=210)
label2 = Label(root,text="This is how you show image in python")
label2.place(x=270,y=399)

root.mainloop()