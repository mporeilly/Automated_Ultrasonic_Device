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
import time
import RPi.GPIO as GPIO
GPIO.cleanup()

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

        scan = df["Scan Area"]   # df is the variable name and .scan_area is the column header 
        X = df["X Coordinate"]
        Y = df["Y Coordinate"]
        Z = df["Voltage Reading"]
        units = df["Measurement Units"]

        previous_scan_unit = units[1]
        print(previous_scan_unit)
        previous_scan_name = scan[1]
        print(previous_scan_name)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')       #     https://stackoverflow.com/questions/51891538/create-a-surface-plot-of-xyz-altitude-data-in-python
        ax.plot_trisurf(X, Y, Z, cmap='RdYlGn')#, edgecolors='grey', alpha=0.5)
        ax.scatter(X, Y, Z, c='black')
        ax.set_title('Data Collected from Scan ' + str(previous_scan_name))
        ax.set_xlabel('Transducer Displacement (' + str(previous_scan_unit) +')')
        ax.set_ylabel('Machine Displacement (' + str(previous_scan_unit) +')')
        ax.set_zlabel('Material Thickness (' + str(previous_scan_unit) +')')

        plt.show()
        root.destroy()
        


def scan_values_func():
    i = 1
    while i > 100:
        print("Current Voltage Reading " + scan_voltage() + 'V')
        time.sleep(0.5)
        i=i+1


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