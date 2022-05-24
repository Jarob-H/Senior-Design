# CNC Window Cleaner Project

![Dependence: Nanpy](https://img.shields.io/librariesio/github/nanpy/nanpy?label=Nanpy)

This project is our team's senior design project at the University of Denver. This project goal was to deliver a solution 
that would allow the operators of the school's Machine Shop to see inside the machine during operation. This was not possible before due to coolant 
splashing against the window while the machine is operating. 

This software controls the Wiper via a GUI:
* Controls speed
* Variable duration 
* Status Display
## Documentation
The projects document lives in the [Wiki](https://github.com/Jarob-H/Senior_design/wiki) section of this git .
## Installation
This project relies on [Nanpy](https://github.com/nanpy/nanpy) . Nanpy is a library that use your Arduino as a slave, 
controlled by a master device which is a Raspberry Pi 4 in our system. Follow the readme of Nanpy to install the [Arduino 
firmware](https://github.com/nanpy/nanpy-firmware) and the Nanpy Python library (```pip install nanpy```) onto the Ras Pi.

Ensure that when running the bash script to generate the config file for the Arduino that you select to include the 
stepper library. This allows you to create a stepper object on the Python side and control it through the arduino.

## Collaborators

| Username   |Contribution|Linkedin|Github Link ↘️                |
|------------|---|------|---------------------------|
|Jarob Heffner|Code|www.linkedin.com/in/jarob-heffner-85a880142/|www.github.com/Jarob-H|
|Corey Valenti|UI Development|www.linkedin.com/in/corey-valenti-1aba79193//|www.github.com/CoreyValenti|
|Vivian Nguyen|STL and mechanical Design|www.linkedin.com/in/nguyenvivian28||
|Isabel Montefinese|STL and mechanical Design|https://www.linkedin.com/in/isabel-montefinese/||
