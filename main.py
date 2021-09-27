import tkinter as tk
from tkinter import *

def end():
    quit()



window = tk.Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))


quit_butt = tk.Button(master=window, text="quit", command=end,height= 7,width=14, bg="red",
    fg="white",padx=100, pady=100)

quit_butt.grid(column=1, row=1)


window.mainloop()