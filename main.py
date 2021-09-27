import tkinter as tk
from tkinter import *

def end():
    quit()



window = tk.Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

quit_butt= tk.Button(master=window, text="quit", command=end)
quit_butt.grid(row=0, column=0, sticky="nsew")

window.mainloop()