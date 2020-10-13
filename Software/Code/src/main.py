# This will be the file that is run on startup of the machine
# likely bash scripting will be needed to start this at start up
# will need an option to exit the startup of the bash script in the event the raspberrypi is being updated


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# user selected nominal thickness of plate
nominal_thickness = 2


# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
class DataPoint:

    def __init__(self, measurement, x_coordinate, y_coordinate):
        self.measurement = measurement
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        # should add a color to the data point for displaying later

    def percentage_remaining(self):
        self.measurement = int(self.measurement / nominal_thickness * 100)

    # def measurement(self):                          #creating a method to pull the data points
    # return self.measurement()


# data intake section
# setup interface for the usb to send data to this code
# this section will need to match the baud rate of the information from the serial port on the scope
# there will need to be processing of the data delivered where the lowest value acquired is set to measurement

data1 = DataPoint(2.1, 4, 6)

print(data1.measurement)
print(data1.percentage_remaining())

# build matrix to place the data points in to their respective places


# build user interface
# create a matrix which is able to display the
