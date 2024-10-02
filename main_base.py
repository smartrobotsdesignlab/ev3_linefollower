#!/usr/bin/env pybricks-micropython

"""
Example created based on LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.parameters import Button

from pybricks.tools import StopWatch, DataLog, wait

# Initialize the brick 
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)


#Calculate the light threshold. Choose values based on your measurements.
BLACK = 7
WHITE = 70
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 300.0
    

# Start following the line endlessly.
while True:
    
    current_value = line_sensor.reflection()
    
    # This will drive both motors at the same speed
    
    left_motor.run(DRIVE_SPEED)
    right_motor.run(DRIVE_SPEED)
    
    # You can wait for a short time or do other things in this loop.
    wait(10)
left_motor.stop()
right_motor.stop()