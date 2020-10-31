# This will be the file that is run on startup of the machine
# likely bash scripting will be needed to start this at start up
# will need an option to exit the startup of the bash script in the event the raspberrypi is being updated

# import statements for the normal modules
#import csv    # this was moved to the required function

# import statements for the functions that we write
import csv_function_file

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
class DataPoint:                                                        # defining class for data collected
    # user selected nominal thickness of plate
    # will look to pull from user within the gui
    nominal_thickness = 2
    units = 'mm'

    def __init__(self, measurement, x_coordinate, y_coordinate):        # defining objects for the class
        self.measurement = measurement
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.percentage = self.measurement / self.nominal_thickness * 100  # need to specify significant digits
        self.units = self.units
        # should add a color to the data point for displaying later


# data intake section
# setup interface for the usb to send data to this code
# this section will need to match the baud rate of the information from the serial port on the scope
# there will need to be processing of the data delivered where the lowest value acquired is set to measurement

data1 = DataPoint(1.4, 4, 6)
data2 = DataPoint(1.934,3,4)

# move into a a function for recording data
#https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
test_value_matrix = []                  # initalizing the array

test_value_matrix.append(data1)         # this creates an arrays of objects
test_value_matrix.append(data2)         # appending instances to list

file_name = input('pick file name: ') # asking the user for the file name of the csv file
csv_function_file.save_csv_file_func(test_value_matrix,file_name + '.csv') # calling the fucntion from the file csv_function_file

# build user interface
# create a matrix which is able to display the