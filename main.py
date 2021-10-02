import tkinter as tk #lib for ui
#three default speeds,off/cutom

hig =11
wide = 27

def end(): #funtc called by quit button
    quit()

def low():#funtc called by print button
    print("Speed: Low")
def med():#funtc called by print button
    print("Speed: Med")
def high():#funtc called by print button
    print("Speed: High")

window = tk.Tk() #creating window ui instance
width, height = window.winfo_screenwidth(), window.winfo_screenheight() #setting ui screen to fill screen

window.geometry('%dx%d+0+0' % (width,height))#setting ui size

low_button= tk.Button(master=window, text="LOW", command=low,height= hig , width=wide, bg="blue",
    fg="white")
med_button= tk.Button(master=window, text="MED", command=med,height= hig,width=wide, bg="blue",
    fg="white")
high_button= tk.Button(master=window, text="High", command=high,height= hig,width=wide, bg="blue",
    fg="white")



off_button = tk.Button(master=window, text="OFF", command=end,height= hig,width=wide, bg="red",
    fg="white")

low_button.grid(column=0, row=0,padx=1, pady=5)
med_button.grid(column=1, row=0,padx=1)
high_button.grid(column=2, row=0,padx=1)
off_button.grid(column=1, row=1)



window.mainloop() #runs ui
