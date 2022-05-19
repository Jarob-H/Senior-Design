import threading
import tkinter as tk
from nanpy import SerialManager, Stepper, ArduinoApi

####
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=410)
canvas.grid(columnspan=2, rowspan=2)
canvas.configure(bg='grey')


class myThread(threading.Thread):
    def __init__(self, stepper,microsteps):
        super().__init__()
        self.stopped = False #init flag to terminate thread
        self.stepper = stepper #makes local stepper
        base= 9000
        self.distance=microsteps*base

    def run(self):#main thread function
        while not self.stopped:
            Stepper.step(self.stepper, -self.distance)  #moves stepper
            Stepper.step(self.stepper, self.distance)

    def stop(self):#method that terminates
        self.stopped = True


class motor:
    def __init__(self):
        limitSwitch=13 #makes a pin for limit switch
        c = SerialManager(device='/dev/ttyACM0')#use nanpy to create an object that communicates with arduino
        self.a = ArduinoApi(connection=c)#connencts to the arduino using connection object
        self.a.pinMode(limitSwitch, self.a.INPUT)#inits a pin on the arduino to track limit swicth
        self.speed = 600 # starting speed set to 600 rpms
        self.microSteps = 1/(1/2)#1/microSteps. Example 1/halfstep
        self.stepsPerRev= 200*self.microSteps#base 200 stepsPerRev
        self.myStepper = Stepper(self.stepsPerRev, 8, 9, speed=self.speed, pin3=10, pin4=11)#sets up stepper object.(steps per revs,pins,pins,initial speed
        self.stopped = False
        self.x = myThread(self.myStepper)#inits threads


    def startMotor(self):
        self.x.start()#starts the thread

    def home(self):
        Stepper.setSpeed(self.myStepper, 100)
        while(self.a.digitalRead(13)!= 1):
            self.myStepper.step(50)

    def stop(self):
        self.x.stop()
        self.x = myThread(self.myStepper,self.microSteps)


    def increase_speed(self):
        self.stop()
        self.speed = self.speed + 200
        Stepper.setSpeed(self.myStepper, self.speed)
        self.startMotor()

    def decrease_speed(self):
        self.stop()
        self.speed = self.speed - 200
        Stepper.setSpeed(self.myStepper, self.speed)
        self.startMotor()


def main():
    # Start button
    motorClass = motor()
    start_text = tk.StringVar()
    start_btn = tk.Button(root, textvariable=start_text, command=lambda: motorClass.startMotor(), font="Raleway",
                          bg="#000000",
                          fg="white",
                          height=9, width=35)
    start_text.set("Start")
    start_btn.grid(column=1, row=0)

    # Stop button
    stop_text = tk.StringVar()
    stop_btn = tk.Button(root, textvariable=stop_text, command=lambda: motorClass.stop(), font="Raleway", bg="#000000",
                         fg="white",
                         height=9, width=35)
    stop_text.set("Stop")
    stop_btn.grid(column=1, row=1)

    # Increase button
    increase_text = tk.StringVar()
    increase_btn = tk.Button(root, textvariable=increase_text, command=lambda: motorClass.increase_speed(),
                             font="Raleway",
                             bg="#000000",
                             fg="white", height=9, width=35)
    increase_text.set("Increase")
    increase_btn.grid(column=0, row=0)

    # Decrease button
    decrease_text = tk.StringVar()
    decrease_btn = tk.Button(root, textvariable=decrease_text, command=lambda: motorClass.decrease_speed(),
                             font="Raleway",
                             bg="#000000",
                             fg="white", height=9, width=35)
    decrease_text.set("Decrease")
    decrease_btn.grid(column=0, row=1)

    root.mainloop()


if __name__ == "__main__":
    main()