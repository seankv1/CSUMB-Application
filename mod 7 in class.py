from tkinter import *
from tkinter.ttk import *
from openpyxl import workbook, load_workbook
import pandas as pd
from PIL import Image, ImageTk


root = Tk()
root.title('CSUMB Application')
root.geometry("500x500")
root.resizable(0, 0)

picture = Image.open("csumbtransparent.png")
picture1 = picture.resize((100, 100), Image.ANTIALIAS)
picture2 = ImageTk.PhotoImage(picture1)
label1=Label(root, image = picture2).place(x=200, y =10)

def apple():
    data = pd.read_excel("csumb.xlsx")
    df =pd.DataFrame(data, columns=['Calendar'])
    lb.config(text = df)

b1 =Button(text = "Calendar", command =apple)
b1.place(x=110, y = 70)
lb = Label(font=("Arial", 15), text = "Output").place(x=125, y=130)

def apple1():
    data = pd.read_excel("hello1.xlsx")
    df =pd.DataFrame(data1, colums=['StudentName'])
    lb.config(text = col)
root.mainloop()

b2 =Button(text = "Student Name", command =apple)
b2.place(x=220, y = 70)
lb = Label(font=("Arial", 15), text = "Output").place(x=125, y=130)

