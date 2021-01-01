# This will be the file that is run on startup of the machine
# likely bash scripting will be needed to start this at start up
# will need an option to exit the startup of the bash script in the event the raspberrypi is being updated

# import statements for the functions that we write
import tkinter as tk                                    # import the package for the window 
import csv_function_file                                # import the custom function for saving to csv file 
# placeholder for start function    needs a stop flag/ command needs to fit into chase's code need it to return the array of data 
# placeholder for the save feature     

root = tk.Tk()                                          # root is the window similar to index.html
root.title('Scanner Application')                       # header info
root.geometry('800x480')                                # window size 

# apparently the text being white is an OSX problem should be fine on the linux distrubution
# https://www.reddit.com/r/learnpython/comments/8tso7e/cannot_change_background_color_of_tkinter_buttons/

# initalization of the units indicator
milimeter_selection = tk.IntVar()                       # createion of the unit boolean indicator

print(milimeter_selection.get())                        # the value starts off at 0 this will be used for the selection statements to make sure teh user inputs correct data
def clicked(value): 
    if value == 1:                                      # value of 1 indicates inches is selected
        print(value,'inches')      
    else:
        print(value,'mm')


unit_selector1 = tk.Radiobutton(root, text=' mm ', variable=milimeter_selection, value=2, command=lambda: clicked(milimeter_selection.get()))
unit_selector1.grid(row=3, column=1)
unit_selector2 = tk.Radiobutton(root, text=' in ', variable=milimeter_selection, value=1, command=lambda: clicked(milimeter_selection.get()))
unit_selector2.grid(row=4, column=1)

myLabel = tk.Label(root, text='Unit Selection:')        # labels the unit selection area of the GUI
myLabel.grid(row=3, column=0)

openfile_button = tk.Button(root, text='Open File')     # creates the button
openfile_button.grid(row=1, column=0)

savefile_button = tk.Button(root, text='Save File')
savefile_button.grid(row=1, column=1)

runscan_button = tk.Button(root, text='Run Scan')
runscan_button.grid(row=1, column=2)

stopscan_button = tk.Button(root, text='Stop Scan')
stopscan_button.grid(row=1, column=3)


root.mainloop() # starts the pop up window






# # https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer
# class DataPoint:                                                        # defining class for data collected
#     # user selected nominal thickness of plate
#     # will look to pull from user within the gui
#     nominal_thickness = 2
#     units = 'mm'

#     def __init__(self, measurement, x_coordinate, y_coordinate):        # defining objects for the class
#         self.measurement = measurement
#         self.x_coordinate = x_coordinate
#         self.y_coordinate = y_coordinate
#         self.percentage = self.measurement / self.nominal_thickness * 100  # need to specify significant digits
#         self.units = self.units
#         # should add a color to the data point for displaying later


# # data intake section
# # setup interface for the usb to send data to this code
# # this section will need to match the baud rate of the information from the serial port on the scope
# # there will need to be processing of the data delivered where the lowest value acquired is set to measurement

# data1 = DataPoint(1.4, 4, 6)
# data2 = DataPoint(1.934,3,4)

# # move into a a function for recording data
# #https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/
# test_value_matrix = []                  # initalizing the array

# test_value_matrix.append(data1)         # this creates an arrays of objects
# test_value_matrix.append(data2)         # appending instances to list

# file_name = input('pick file name: ') # asking the user for the file name of the csv file
# csv_function_file.save_csv_file_func(test_value_matrix,file_name + '.csv') # calling the fucntion from the file csv_function_file

# # build user interface
# # create a matrix which is able to display the

# #https://pimylifeup.com/raspberry-pi-on-screen-keyboard/