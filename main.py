import tkinter as tk #lib for ui

def end(): #funtc called by quit button
    quit()

def print_fun():#funtc called by print button
    print("hello")

window = tk.Tk() #creating window ui instance
width, height = window.winfo_screenwidth(), window.winfo_screenheight() #setting ui screen to fill screen

window.geometry('%dx%d+0+0' % (width,height))#setting ui size

print_button= tk.Button(master=window, text="Hit to print", command=print_fun,height= 4,width=8, bg="blue",
    fg="white",padx=100, pady=100)


quit_button = tk.Button(master=window, text="quit", command=end,height= 4,width=8, bg="red",
    fg="white",padx=100, pady=100)

print_button.grid(column=0, row=0)
quit_button.grid(column=2, row=0)


window.mainloop() #runs ui
