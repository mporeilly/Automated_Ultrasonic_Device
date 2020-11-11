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

# Stepper Motor control (wheels)

# install/import libraries (RPi.GPIO, time, gpiozero?) as GPIO

# import pip
# pip install RPi.GPIO
# import RPi.GPIO as GPIO   ;not sure if this works

# No finalized motor specs yet
# for now assume 2048 steps/rev. Half stepping for more precision (4096 steps/rev)

# Assign 4 gpio pins as output
output = [1, 2, 3, 4]  # list of the 4 gpio pins that will be used as outputs, not sure of actual pin numbers rn

# create 8x4 array representing the sequence of pin activation for half stepping. Assuming dual phase
sequence = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0],
           [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]  # 4 pins, 8 (half) steps

# convert linear distance that we want to move into degrees of rotation, then degrees into "x" steps
# create nested for-loop that energizes the pins in order (using the sequence array) to move the stepper "x" steps
# initialize variable for number of 8 step cycles it will take to turn our desired unit distance
# with the dummy specs outlined, 512 cycles = 360 degrees full revolution, obviously we need much less

cycles = 512

for spin in range(cycles):  # loops through the number of 8 step cycles desired
    for step in range(8):  # looping through the 8 half steps
        for pin in range(4):  # looping through the pins 1 to 4 (index 0 to 3 of the list)
            GPIO.output(output[pin], sequence[step][pin])  # Sets each pin output in sequence, library based command


# may have to play around with different time delays, optimize for speed/torque
# will have to repeat this block of code each time the device is done scanning in the x direction
# Causes device to inch forward in the y direction before scanning again in the x direction (serpentine scanning path)
