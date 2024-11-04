import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("digital clock")

def newTime():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,newTime)

label = tk.Label(root, font=('calibri',50,'bold'),background='yellow',foreground='black')
label.pack(anchor='center')

newTime()

root.mainloop()