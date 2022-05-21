# CNC Window Cleaner Project
This project is our team's senior design project at the University of Denver. This project goal was to deliver a solution 
that would allow the operators of the school's Machine Shop to see inside the machine during operation. This was not possible before due to coolant 
splashing against the window while the machine is operating. 

This software controls the Wiper via a GUI:
* Controls speed
* Variable duration 
* Status Display

## Installation
This project relies on [Nanpy](https://github.com/nanpy/nanpy) . Nanpy is a library that use your Arduino as a slave, 
controlled by a master device which is a Raspberry Pi 4 in our system. Follow the readme of Nanpy to install the [Arduino 
firmware](https://github.com/nanpy/nanpy-firmware) and the Nanpy Python library (```pip install nanpy```) onto the Ras Pi.

## Thread Class
This class is used to run one thread in the background. This thread's purpose is to run one cycle of the
wiper(up and down). By running this operation in a thread the UI is able to countiue to run on the main thread and
change the status if needed.

### run():
The run function is the main function of the thread that is executed when the thread is started. It runs in a loop
that looks for a flag to see if the thread has been stopped.It uses the stepper object that is passed in as a parameter 
into the thread class. 

## UI Class
The operations for the CNC window wiper will be controlled on a raspberry pi 4 and 7in touch screen that is mounted on 
the outside the CNC machine.


The UI will have the following operations:
* Turn on the wipers to one of the default speeds (Slow, medium, fast)
* Turn off the wipers
* Prompt the user for a speed and amount of time they would like to run them

### window Function:
This function is the main function for the UI it creates the main window that runs the UI. It creates and laysout the button
and defines what function to execute when pressed.

### low/Medium/high functions:
These functions are functions that are executed when the respective button is pressed. They then set the varibles 
to preset values that are defined for each function. Finally, they call the Update function

### update():
This function is used to update the status panel displayed on the UI


This code is used to redefine the status variable displayed on the main UI screen by reconfiguring the text displayed.

