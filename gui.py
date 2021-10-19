from tkinter import *
from tkinter import filedialog
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb 
base = Tk()
base.geometry('500x500')
base.config(bg=rgb_hack((170,250,100)))
def file_opener():
   input = filedialog.askopenfile(initialdir="/")
   for i in input:
       print(i)
x = Label(base, text="Welcome to Resume Screening",font=("Arial", 25))
x.pack()
x.place(x=20, y=50)
x = Button(base, text ='Select a .txt/.csv file', command = lambda:file_opener(), pady=10, padx=10, font=("Arial", 20))
x.pack()
x.place(x=120, y=220)
x = Button(base, text ='EXIT', command = base.destroy, pady=10, padx=10, font=("Arial", 20))
x.pack()
x.place(x=210, y=400)




