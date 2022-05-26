import threading
import tkinter as tk
from tkinter import *
from nanpy import SerialManager, Stepper, ArduinoApi


class myThread(threading.Thread):
    def __init__(self, stepper, microsteps):
        super().__init__()
        self.stepper = stepper  # makes local stepper
        base = 9000
        self.distance = microsteps * base
        self._running = True

    def run(self):  # main thread function
        while self._running:
            Stepper.step(self.stepper, -self.distance)  # moves stepper
            Stepper.step(self.stepper, self.distance)

    def terminate(self):
        self._running = False


class motor:
    def __init__(self):
        self.limitSwitch = 13  # makes a pin for limit switch
        c = SerialManager(device='/dev/ttyACM0')  # use nanpy to create an object that communicates with arduino
        self.a = ArduinoApi(connection=c)  # connencts to the arduino using connection object
        self.a.pinMode(self.limitSwitch, self.a.INPUT)  # inits a pin on the arduino to track limit swicth
        self.speed = 600  # starting speed set to 600 rpms
        self.microSteps = 1 / (1 / 2)  # 1/microSteps. Example 1/halfstep
        self.stepsPerRev = 200 * self.microSteps  # base 200 stepsPerRev
        self.myStepper = Stepper(self.stepsPerRev, 8, 9, speed=self.speed, pin3=10,
                                 pin4=11)  # sets up stepper object.(steps per revs,pins,pins,initial speed
        self.stopped = False
        self.x = myThread(self.myStepper, self.microSteps)  # inits threads

    def startMotor(self):
        if not self.x.is_alive():
            self.x.start()  # starts the thread

    def home(self):
        Stepper.setSpeed(self.myStepper, 100)
        while (self.a.digitalRead(self.limitSwitch) != 1):
            self.myStepper.step(50 * self.microSteps)

    def stop(self):
        if self.x.is_alive():
            self.x.terminate()  # calls funtion that sets class flag to terminate thread
            self.home()

    def increase_speed(self):
        if (self.speed < 800):  # checks to see if the speed is over 800
            self.stop()
            self.speed = self.speed + 200  # increase the speed by 200
            Stepper.setSpeed(self.myStepper, self.speed)  # set speed
            self.startMotor()

    def decrease_speed(self):
        if (self.speed > 600):  # checks to see if the speed is under 600
            self.stop()
            self.speed = self.speed - 200  # decress the speed by 200
            Stepper.setSpeed(self.myStepper, self.speed)  # set speeds
            self.startMotor()


def main():
    ###
    root = tk.Tk()
    canvas = tk.Canvas(root, width=800, height=480, cursor='cross')
    root.attributes('-fullscreen', True)  # makes fullscreen on PI
    canvas.grid(columnspan=2, rowspan=3)
    canvas.configure(bg='#3A3B3C')

#Start button
    motorClass = motor()
    start_text = tk.StringVar()
    start_btn = tk.Button(root, textvariable=start_text, command=lambda: motorClass.startMotor(), font="Raleway",
                          bg="#000000",
                          bd=5,
                          fg="white",
                          activebackground='grey',
                          cursor='cross',
                          height=7, width=33)
    start_text.set("Start")
    start_btn.grid(column=1, row=0)

#Stop button
    stop_text = tk.StringVar()
    stop_btn = tk.Button(root, textvariable=stop_text, command=lambda: motorClass.stop(), font="Raleway", bg="#000000",
                         bd=5,
                         fg="white",
                         activebackground='grey',
                         cursor='cross',
                         height=7, width=33)
    stop_text.set("Stop")
    stop_btn.grid(column=1, row=2)

#Increase button
    increase_text = tk.StringVar()
    increase_btn = tk.Button(root, textvariable=increase_text, command=lambda: motorClass.increase_speed(),
                             font="Raleway",
                             bg="#000000",
                             bd=5,
                             activebackground='grey',
                             cursor='cross',
                             fg="white", height=7, width=33)
    increase_text.set("Increase")
    increase_btn.grid(column=0, row=0)

#Decrease button
    decrease_text = tk.StringVar()
    decrease_btn = tk.Button(root, textvariable=decrease_text, command=lambda: motorClass.decrease_speed(),
                             font="Raleway",
                             bg="#000000",
                             bd=5,
                             activebackground='grey',
                             cursor='cross',
                             fg="white", height=7, width=33)
    decrease_text.set("Decrease")
    decrease_btn.grid(column=0, row=2)
    
#Slider
    font1=('Raleway', 22, 'bold')
    slider = tk.Tk()
    sc=tk.Scale(from_=0, to=1200, activebackground='grey', sliderlength=30, bd=5, bg='black', fg='white', orient='horizontal', cursor='cross', font=font1, length=353, width=50)
    sc.grid(column=0, row=1)
    root.mainloop()


if __name__ == "__main__":
    main()
