# CNC Window Cleaner Project

## Overview
***
This project is my senior design project. This project goal was to deliver a solution that would allow the operators of 
the school's Machine Shop to see inside the machine during operation. This was not possible before due to coolant 
splashing against the window while the machine is operating. 

## SERIAL Class
***
This clas contians all funtions needed for the microprossor(RasPi) to communicate with the microcontrollor(Pi Pico). The main 
advantage to this is the Ras Pi can be outside of the the CNC attached to the UI touch screen and will send commands to the MC
inside of the CNC via a usb serial connection. This eliminates the need to run multiple wires for each of GPIOs needed.

### readSerial Function:
This function is used receive data back from the MP. It will be used to report after a sequince is complete, 
report the current status of the  wiper, and return other infomation that may be applitable.

### sendSerial Function:
This function's purpose is to send commands from the MC to the MP. This allows the MP to be the brains of the machine and
the MC simple execute the commands sent. This allows for a quick gpio access. 

## UI Class
***
The operations for the CNC window wiper will be controlled on a raspberry pi 4 and 7in touch screen that is mounted on 
the outside the CNC machine. 

The UI will have the following operations:
* Turn on the wipers to one of the default speeds (Slow, medium, fast)
* Turn off the wipers
* Prompt the user for a speed and amount of time they would like to run them