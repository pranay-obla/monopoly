import PIL.Image, PIL.ImageTk
from tkinter import *

root1=Tk()
root1.geometry('1000x400')
root1.title('Monopoly')
root1.configure(bg='black')

load=PIL.Image.open('newhome.png')
ren=PIL.ImageTk.PhotoImage(load)
img=Label(root1,image=ren,borderwidth=0)
img.image=ren
img.pack(side='top',anchor=CENTER)

root1.mainloop()