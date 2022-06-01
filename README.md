# CNC Window Cleaner Project

![Dependence: Nanpy](https://img.shields.io/librariesio/github/nanpy/nanpy?label=Nanpy)

This project is our team's senior design project at the University of Denver. The project's goal was to deliver a solution 
that would allow the operators of the school's Machine Shop HAAS Mini Mill to see inside the machine during operation. Prior to our project the user would struggle to see the part they were milling due to coolant splashing against the window while the machine is operating. 

This software controls the Wiper via a GUI:
* Speed Control 
* Start
* Home 

## Documentation
The projects document lives in the [Wiki](https://github.com/Jarob-H/Senior_design/wiki) section of this git .
## Installation
This project relies on [Nanpy](https://github.com/nanpy/nanpy) . Nanpy is a library that use your Arduino as a slave, 
controlled by a master device which is a Raspberry Pi 4 in our system. Follow the readme of Nanpy to install the [Arduino 
firmware](https://github.com/nanpy/nanpy-firmware) and the Nanpy Python library (```pip install nanpy```) onto the Ras Pi.

Ensure that when running the bash script to generate the config file for the Arduino that you select to include the 
stepper library. This allows you to create a stepper object in your Python script and control the stepper through the arduino.

## Future Expansion
We hope to continue to exand the software funtionality by adding addition feature.

Features we hope to add in the future:
* Variable duration settings
* Automatic start and stop when door is open or moisture is detected
* Intergrated controls with HAAS Mini Mill utilizing system's Gcode

## Collaborators

| Username   |Contribution|Linkedin|Github Link ↘️                |
|------------|---|------|---------------------------|
|Jarob Heffner|Code|www.linkedin.com/in/jarob-heffner-85a880142/|www.github.com/Jarob-H|
|Corey Valenti|UI Development|www.linkedin.com/in/corey-valenti-1aba79193//|www.github.com/CoreyValenti|
|Vivian Nguyen|STL and mechanical Design|www.linkedin.com/in/nguyenvivian28||
|Isabel Montefinese|STL and mechanical Design|https://www.linkedin.com/in/isabel-montefinese/||
