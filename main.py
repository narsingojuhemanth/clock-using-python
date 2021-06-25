from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("        CLOCK       ")

def time():
    string=strftime('  %Y:%m:%d \n %H:%M:%S  %p')
    label.config(text=string)
    label.after(1000,time)

label=Label(root, font=("DS-Digital",100), background="black", foreground="#03A062")
label.pack(anchor="center")
time()

mainloop()

