import threading
import tkinter as tk
from nanpy import SerialManager, Stepper, ArduinoApi

####
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=410)
canvas.grid(columnspan=2, rowspan=2)
canvas.configure(bg='grey')


class myThread(threading.Thread):
    def __init__(self, stepper):
        super().__init__()
        self.stopped = False
        self.stepper = stepper

    def run(self):
        while not self.stopped:
            Stepper.step(self.stepper, -9000)  #
            Stepper.step(self.stepper, 9000)

    def stop(self):
        self.stopped = True


class motor:
    def __init__(self):
        c = SerialManager(device='/dev/ttyACM0')#use nanpy to create an object that communicates with arduino
        self.a = ArduinoApi(connection=c)
        self.a.pinMode(13, self.a.INPUT)

        self.speed = 600
        self.myStepper = Stepper(200, 8, 9, speed=0, pin3=10, pin4=11)
        Stepper.setSpeed(self.myStepper, self.speed)
        self.stopped = False
        self.x = myThread(self.myStepper)

    def startMotor(self):
        self.x.start()

    def home(self):
        Stepper.setSpeed(self.myStepper, 100)
        while(self.a.digitalRead(13)!= 1):
            self.myStepper.step(50)

    def stop(self):
        self.x.stop()
        self.x = myThread(self.myStepper)


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