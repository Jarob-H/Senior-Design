import tkinter as tk  # lib for ui


# three default speeds,off/cutom


class UI:
    def __init__(self):
        self.time = 0
        self.speed = 0
        self.buttonWidth = 29
        self.buttonHeight = 10
        self.windowHeight=0
        self.windowWidth=0
        self.window()

    def window(self):
        window = tk.Tk()  # creating window ui instance
        self.windowWidth, self.windowHeight = window.winfo_screenwidth(), window.winfo_screenheight()  # setting ui screen to fill screen

        window.geometry('%dx%d+0+0' % (self.windowWidth, self.windowHeight))  # setting ui size

        low_button = tk.Button(master=window, text="LOW", command=self.low, height=self.buttonHeight,
                               width=self.buttonWidth, bg="blue",
                               fg="white")
        med_button = tk.Button(master=window, text="MED", command=self.med, height=self.buttonHeight,
                               width=self.buttonWidth, bg="blue",
                               fg="white")
        high_button = tk.Button(master=window, text="High", command=self.high, height=self.buttonHeight,
                                width=self.buttonWidth, bg="blue",
                                fg="white")

        custom_button = tk.Button(master=window, text="CUSTOM", command=self.open_popup, height=self.buttonHeight,
                               width=self.buttonWidth, bg="yellow",
                               fg="white")

        off_button = tk.Button(master=window, text="OFF", command=self.end, height=self.buttonHeight,
                               width=self.buttonWidth, bg="red",
                               fg="white")

        low_button.grid(column=0, row=0, padx=2, pady=5)
        med_button.grid(column=1, row=0, padx=2)
        high_button.grid(column=2, row=0, padx=2)
        custom_button.grid(column=1, row=1)
        off_button.grid(column=2, row=1)

        window.mainloop()  # runs ui

    def end(self):  # funtc called by quit button
        quit()

    def low(self):  # funtc called by print button
        print("Speed: Low")

    def med(self):  # funtc called by print button
        print("Speed: Med")

    def high(self):  # funtc called by print button
        print("Speed: High")

    def open_popup(self):
        popup=tk.Tk()
        popup.geometry('%dx%d+0+0' % (self.windowWidth,self.windowHeight))  # setting ui size
        label = tk.Label(popup, text='error')
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()


def main():
    print("Hello World!")
    ui = UI()


if __name__ == "__main__":
    main()
