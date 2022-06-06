import threading
import tkinter as tk
from nanpy import SerialManager, Stepper, ArduinoApi

####
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=410)
canvas.grid(columnspan=2, rowspan=2)
canvas.configure(bg='grey')




class Ui():
    def __init__(self, root,motorClass):
        super().__init__()

        canvas = tk.Canvas(root, width=800, height=480, cursor='cross')
        root.attributes('-fullscreen', True)  # makes fullscreen on PI
        canvas.grid(columnspan=2, rowspan=3)
        canvas.configure(bg='#3A3B3C')

        start_text = tk.StringVar()
        start_btn = tk.Button(root, textvariable=start_text, font="Raleway",
                              bg="#000000",
                              bd=5,
                              fg="white",
                              activebackground='grey',
                              cursor='cross',
                              height=7, width=33)
        start_text.set("Start")
        start_btn.grid(column=1, row=0)

        # Stop button
        stop_text = tk.StringVar()
        stop_btn = tk.Button(root, textvariable=stop_text, font="Raleway", bg="#000000",
                             bd=5,
                             fg="white",
                             activebackground='grey',
                             cursor='cross',
                             height=7, width=33)
        stop_text.set("Stop")
        stop_btn.grid(column=1, row=2)

        # Increase button
        increase_text = tk.StringVar()
        increase_btn = tk.Button(root, textvariable=increase_text,
                                 font="Raleway",
                                 bg="#000000",
                                 bd=5,
                                 activebackground='grey',
                                 cursor='cross',
                                 fg="white", height=7, width=33)
        increase_text.set("Increase")
        increase_btn.grid(column=0, row=0)

        # Decrease button
        decrease_text = tk.StringVar()
        decrease_btn = tk.Button(root, textvariable=decrease_text, command=lambda:printer(self.val),
                                 font="Raleway",
                                 bg="#000000",
                                 bd=5,
                                 activebackground='grey',
                                 cursor='cross',
                                 fg="white", height=7, width=33)
        decrease_text.set("Decrease")
        decrease_btn.grid(column=0, row=2)

        # Slider

        font1 = ('Raleway', 22, 'bold')
        self.slider = tk.Scale(from_=0, to=1200, activebackground='grey', sliderlength=30, bd=5, bg='black', fg='white',
                               orient='horizontal', cursor='cross', font=font1, length=353, width=50,
                               command=self.updateVal)
        self.val = self.slider.get()
        self.slider.grid(column=0, row=1)

    def updateVal(self, event):
        self.val = self.slider.get()

    def setVal(self, val):
        self.slider.set(val)


def main():
    ###
    motorClass=motor()
    root = tk.Tk()
    ui = Ui(root,motorClass)
    root.mainloop()


if __name__ == "__main__":
    main()
