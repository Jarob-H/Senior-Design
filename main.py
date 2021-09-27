import tkinter as tk

def end():
    quit()


window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="quit", command=end)
btn_decrease.grid(row=0, column=0, sticky="nsew")

window.mainloop()