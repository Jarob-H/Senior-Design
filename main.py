import tkinter as tk #lib for ui
#three default speeds,off/cutom


class UI:

    def __init__(self):
        self.time=0
        self.speed=0
        self.windowwidth=29
        self.windowHeight=10
        self.window()

    def window(self):
        window = tk.Tk() #creating window ui instance
        width, height = window.winfo_screenwidth(), window.winfo_screenheight() #setting ui screen to fill screen

        window.geometry('%dx%d+0+0' % (width,height))#setting ui size

        low_button= tk.Button(master=window, text="LOW", command=self.low,height= self.windowHeight , width=self.windowwidth, bg="blue",
            fg="white")
        med_button= tk.Button(master=window, text="MED", command=self.med,height= self.windowHeight ,width=self.windowwidth, bg="blue",
            fg="white")
        high_button= tk.Button(master=window, text="High", command=self.high,height= self.windowHeight ,width=self.windowwidth, bg="blue",
            fg="white")

        off_button = tk.Button(master=window, text="OFF", command=self.end,height= self.windowHeight ,width=self.windowwidth, bg="red",
            fg="white")

        low_button.grid(column=0, row=0,padx=2, pady=5)
        med_button.grid(column=1, row=0,padx=2)
        high_button.grid(column=2, row=0,padx=2)
        off_button.grid(column=1, row=1)

        window.mainloop() #runs ui

    def end(self):  # funtc called by quit button
        quit()

    def low(self):  # funtc called by print button
        print("Speed: Low")

    def med(self):  # funtc called by print button
        print("Speed: Med")

    def high(self):  # funtc called by print button
        print("Speed: High")

def main():
    print("Hello World!")
    ui =UI()
if __name__ == "__main__":
    main()