import tkinter as tk                                    # import the package for the window 
#import csv_function_file                                # import the custom function for saving to csv file 
from scan_controller import scan_control    
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter.messagebox as tkmb
from analogtodig import scan_voltage
import csv

root = tk.Tk()                                          # root is the window similar to index.html
root.title('Scanner Application')                       # header info
root.geometry('424x150')                                # window size 

# units indicator radio buttons
milimeter_selection = tk.IntVar()                       # creation of the unit indicator starts at 0 with no selection
voltage_selection = tk.IntVar()
operation_flag = 1                                      # this flag means the machine is ready to run
width_textbox = tk.StringVar()
length_textbox = tk.StringVar()
scan_name_textbox = tk.StringVar()                              # allows the user to define scan values

def plotting_of_open_file():                           # this function is used to plot already saved data, historical review 
    file_name = askopenfilename()
    with open(file_name) as csv_file:
        df = pd.read_csv(file_name)

        print(df)
        scan = df.scan_area   # df is the variable name and .scan_area is the column header 
        print(scan)
        X = df.x_coor
        Y = df.y_coor
        Z = df.thickness

        previous_scan_unit = df.units[1]
        previous_scan_name = df.scan_area[1]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')       #     https://stackoverflow.com/questions/51891538/create-a-surface-plot-of-xyz-altitude-data-in-python
        ax.plot_trisurf(X, Y, Z, cmap='RdYlGn')#, edgecolors='grey', alpha=0.5)
        ax.scatter(X, Y, Z, c='black')
        ax.set_title('Data Collected from Scan ' + previous_scan_name)
        ax.set_xlabel('Transducer Displacement (' + previous_scan_unit +')')
        ax.set_ylabel('Machine Displacement (' + previous_scan_unit +')')
        ax.set_zlabel('Material Thickness (' + previous_scan_unit +')')

        plt.show()


def scan_values_func():
    while True:
        tkmb.showinfo("Current Voltage Reading", scan_voltage)


# value of 1 indicates inches is selected

radio_mm = tk.Radiobutton(root, text=' mm ', variable=milimeter_selection, value=1)
radio_mm.grid(row=3, column=1, sticky=tk.W)
radio_in = tk.Radiobutton(root, text=' in ', variable=milimeter_selection, value=2) 
radio_in.grid(row=4, column=1, sticky=tk.W)

# voltage selector 
radio_mm = tk.Radiobutton(root, text=' 0 to 1V ', variable=voltage_selection, value=2) 
radio_mm.grid(row=3, column=3, sticky=tk.W)

myLabel = tk.Label(root, text='Voltage Range:')        # labels the unit selection area of the GUI
myLabel.grid(row=3, column=2)
# scan dimensions 

width_label = tk.Label(root, text='Scan Width:')
width_label.grid(row=5, column=0)

width_textbox = tk.Entry(root, width=7)
width_textbox.grid(row=5, column=1, sticky=tk.W)

length_label = tk.Label(root, text='Scan length:')
length_label.grid(row=6, column=0)

length_textbox = tk.Entry(root, width=7)
length_textbox.grid(row=6, column=1, sticky=tk.W)

scan_name_label = tk.Label(root, text='Scan Name:')
scan_name_label.grid(row=4, column=2)

scan_name_textbox = tk.Entry(root, width=7)
scan_name_textbox.grid(row=4, column=3, sticky=tk.W)

# selection statements which allow the top buttons to be activated

gate_start_label = tk.Label(root, text='Gate Start:')           # this is for tracking the 
gate_start_label.grid(row=5, column=2)
gate_width_label = tk.Label(root, text='Gate Width:')  # span of the thickness from the start
gate_width_label.grid(row=6, column=2)

gate_start_textbox = tk.Entry(root, width=7)
gate_start_textbox.grid(row=5, column=3, sticky=tk.W)

gate_width_textbox = tk.Entry(root, width=7)
gate_width_textbox.grid(row=6, column=3, sticky=tk.W)


# main top buttons 

myLabel = tk.Label(root, text='Unit Selection:')        # labels the unit selection area of the GUI
myLabel.grid(row=3, column=0)

openfile_button = tk.Button(root, text='Open File',command=lambda:plotting_of_open_file())     # creates the button
openfile_button.grid(row=1, column=0)

savefile_button = tk.Button(root, text='Test Calibration',command=lambda:scan_values_func())
savefile_button.grid(row=1, column=1)

runscan_button = tk.Button(root, text='Run Scan', command=lambda: scan_control(width_textbox.get(), length_textbox.get(), gate_start_textbox.get(), gate_width_textbox.get(), milimeter_selection.get(), operation_flag, scan_name_textbox.get()))
runscan_button.grid(row=1, column=2)


# work on pop up to tell the operator to reset the scanner at the origin of the scan
resetscan_button = tk.Button(root, text='Reset Scan', bg='orange')
resetscan_button.grid(row=1, column=3)

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