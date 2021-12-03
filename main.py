import tkinter as tk  # lib for ui


# three default speeds,off/cutom

def readserial():
    input = "x"
def sendSerial(speed,duration):#funtion to send speed and time to microC
    print("Speed:"+str(speed))
    print("Duration:"+str(duration))

class UI:
    def __init__(self):
        self.time = 0
        self.speed = 0
        self.buttonWidth = 29
        self.buttonHeight = 10
        self.windowHeight=0
        self.windowWidth=0
        self.window()
        self.status="OFF"

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
        self.speed=15
        self.duration=100
        sendSerial(self.speed,self.duration)

    def med(self):  # funtc called by print button
        print("Speed: Med")

    def high(self):  # funtc called by print button
        print("Speed: High")

    def open_popup(self):
        popup=tk.Tk()

        tk.Label(popup, text="Speed:").grid(row=0)
        tk.Label(popup, text="Duration").grid(row=1)
        vcmd = (popup.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.e1 = tk.Entry(popup, validate = 'key', validatecommand = vcmd)
        self.e2 = tk.Entry(popup, validate = 'key', validatecommand = vcmd)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)



        tk.Button(popup, text="Confirm", command=lambda:[self.sendCustom(),popup.destroy()],bg="green",
                               fg="white").grid(row=2,column=0)
        tk.Button(popup, text="Cancel", command=popup.destroy,bg="red",
                               fg="white").grid(row=2, column=1)
        popup.mainloop()

    def sendCustom(self):
        sendSerial(self.e1.get(),self.e2.get())


    def validate(self, action, index, value_if_allowed,
                 prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False

def main():
    print("Hello World!")
    ui = UI()


if __name__ == "__main__":
    main()
