# This will be the file that is run on startup of the machine
# likely bash scripting will be needed to start this at start up
# will need an option to exit the startup of the bash script in the event the raspberrypi is being updated



# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
class DataPoint:                                                        # defining class for data collected
    # user selected nominal thickness of plate
    # will look to pull from user within the gui
    nominal_thickness = 2

    def __init__(self, measurement, x_coordinate, y_coordinate):        # defining objects for the class
        self.measurement = measurement
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.percentage = self.measurement / self.nominal_thickness * 100  # need to specify significant digits
        # should add a color to the data point for displaying later



# data intake section
# setup interface for the usb to send data to this code
# this section will need to match the baud rate of the information from the serial port on the scope
# there will need to be processing of the data delivered where the lowest value acquired is set to measurement

data1 = DataPoint(2.1, 4, 6)
data2 = DataPoint(1.934,3,4)

print(data1.percentage)
print(data2.percentage)
# build matrix to place the data points in to their respective places
# creating list

#https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
#list = [data1, DataPoint()]

# appending instances to list

# build user interface
# create a matrix which is able to display the

# Stepper Motor control

# install/import libraries (RPi.GPIO as GPIO)
# import pip
# pip install RPi.GPIO
# import RPi.GPIO as GPIO   ;not sure if this works


radius = 1  # temporary wheel radius
belt = 1  # temporary belt radius
scanPath = 12  # length of scanner path
degrees = 1.8  # degrees per step (for full stepping, half stepping is utilized in the move functions)
distance = 0.75  # desired forward distance per scan, in inches (could make this a user input with GUI)
count = 0  # counts number of scans, used for while-loop exit condition

from WheelStepperFunction2 import movewheels  # importing created functions from external files
from TransducerStepperFunction2 import movescanner

go = 1
direction = "forward"

# forward scan loop
while count < ((scanPath/distance)+1):  # (inches of grid to scan / distance per scan = number of scans) +1 at start
    if go == 1:
        go = 0
        go = movescanner(belt, degrees, scanPath, direction)
        count += 1
    if go == 1:
        go = 0
        direction = "forward"
        go = movewheels(radius, degrees, distance, direction)

        if count % 2 != 0:
            direction = "reverse"
        else:
            direction = "forward"

go = 1
direction = "reverse"
# Implement/verify reverse to origin after forward scan is working
# Reverse scan loop
while count < (
        (12 / distance) + 1):  # (12 inches of grid to scan / distance per scan = number of scans) +1 scan at start
    if go == 1:
        go = 0
        go = movescanner(belt, degrees, scanPath, scannerOutpins, direction)
        count += 1
    if go == 1:
        go = 0
        direction = "reverse"
        go = movewheels(radius, degrees, distance, wheelOutpins, direction)

        if count % 2 != 0:
            direction = "forward"
        else:
            direction = "reverse"

# may have to play around with different time delays, optimize for speed/torque
# Causes device to inch forward in the y direction before scanning again in the x direction (serpentine scanning path)
