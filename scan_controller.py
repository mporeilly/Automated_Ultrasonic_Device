import math
import time
from WheelStepperFunction import movewheels  # importing created functions from external files
from TransducerStepperFunction import movescanner
from analogtodig import scan_voltage
import RPi.GPIO as GPIO
import csv
import serial

def scan_control(width, length, gate_start, gate_width, unit, operation_flag, scan_name):
    # if statement to make sure the values fit within the
    value_matrix = [] # initalizing the array that will hold the DataPoint values
    #GPIO.setmode(GPIO.BCM) # choose the pin numbering    apperently needed to prevent error on line below
    #GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO25 as input (button)


    class DataPoint:                                                        # defining class for data collected
        def __init__(self, scan_file_name, gate_start_value, gate_width_value, x_coordinate, y_coordinate, voltage_data, measurement_thickness, units):        # defining objects for the class
            self.scan_file_name = scan_file_name
            self.voltage_data = voltage_data
            self.gate_start_value = gate_start_value
            self.gate_width_value = gate_width_value
            self.measurement_thickness = measurement_thickness
            self.x_coordinate = x_coordinate
            self.y_coordinate = y_coordinate
            self.units = units

    if unit != 1 and unit != 2:
        return

    if unit == 2:
        radius = 1.5  # wheel radius in inches
        belt = 1  # temporary belt radius in inches
        yincrement = 0.75  # y increment in inches
        unit_text = 'inches'

    if unit == 1:
        radius = 38.1  # wheel radius in mm
        belt = 25.4  # temporary belt radius in mm
        yincrement = 19.05  # y increment in mm
        unit_text = 'mm'

    scanPath = width  # length of scanner path
    degrees = 1.8/2  # degrees per step (for full stepping, half stepping is utilized in the move functions)
    stepincrement = int(yincrement / (degrees * ((2 * math.pi) / 360) * radius))  # number of steps in y increment

        #https://raspi.tv/2013/rpi-gpio-basics-6-using-inputs-and-outputs-together-with-rpi-gpio-pull-ups-and-pull-downs
    # if GPIO.input(17) == 0: # if port 25 == 0
    #         print("zeroing stage hit")
    #         while True:# limit switch GPIO is high:
    #             movescanner(belt, degrees, 1, xdirection)  # moves transducer until switch gpio pulled low?
    #             if GPIO.input(17) == 1:
    #                 break


    # linear interpolation to get the correct thickness from the voltage collected
    def interpolation_func(voltage, gate_start, gate_width):
        thickness = (((voltage*(float(gate_start)+float(gate_width))-float(gate_start)))/(1))+float(gate_start)   # got an non-int of type float error
        return thickness

    def measurement_to_impulse(length):                
        #returns the number of impulses required to drive the
        impulse_number = int(float(length) / (degrees * ((2 * math.pi) / 360) * radius)) # steps per length
        return impulse_number

    def impulse_to_measurement(impulse):               
        #returns the distance from the impulse value
        distance_of_impulse = impulse * (degrees * ((2 * math.pi) / 360) * radius)
        return distance_of_impulse

    length_impulses = measurement_to_impulse(length) / stepincrement # number of forward increments in grid
    width_impulses = measurement_to_impulse(width)  # number of steps per probe sweep
    print(length_impulses)
    print(width_impulses)
    xdirection = 1  # starting direction of probe set to left->right
    ydirection = 1  # starting direction of wheels set to forward
    print(range(int(length_impulses)))
    print('op flag value ' + str(operation_flag))

    # start of csv intialization
    with open(scan_name +'.csv','w') as output_file:      # output_file is a variable for the file being exported w means write
        csv_writer = csv.writer(output_file, delimiter=',')  # assigning a variable to control the format of the file exported
        csv_writer.writerow(['Scan Area','Gate Start','Gate Width','X Coordinate','Y Coordinate','Voltage Reading','Measurement Value','Measurement Units']) # this info needs to be lower case for the open saved data function to work properly
        
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        while operation_flag == 1:  # this is for the emergency stop to be wired to

            for y_movement in range(int(length_impulses)+1):

                if y_movement > 0:
                    movewheels(radius, degrees, yincrement, ydirection)
                    print('y move ' + str(y_movement))

                if y_movement == length_impulses:  # when length is reached, reverse wheel direction
                    ydirection = 0


                if y_movement % 2 != 0:  # this reverses x direction after each probe sweep
                    xdirection = 0

                else:
                    xdirection = 1

                for x_movement in range(int(width_impulses)):
                    
                    movescanner(belt, degrees, width_impulses, xdirection)
                    print(str(y_movement) + ' is y impulse and width (x) impulse is ' + str(x_movement)) 
                    
                    voltage = scan_voltage(ser)
                    print(voltage)                                     # value delivered from the function is a string converted to float for math
                    thickness = interpolation_func(float(voltage), gate_start, gate_width)
                    
                    if (x_coordinate % 2) > 0: # need to account for the serpintine path back
                        x_coordinate = impulse_to_measurement(int(width_impulses)-x_movement)                           # need to account for the path back
                    else:
                        x_coordinate = impulse_to_measurement(x_movement)

                    y_coordinate = impulse_to_measurement(y_movement)       
                    value_matrix.append(DataPoint(scan_name, gate_start, gate_width, x_coordinate, y_coordinate, voltage, thickness, unit_text))
                    
                for line in value_matrix:                      # looping through the lines in the test matrix
                    csv_writer.writerow([line.scan_file_name, line.gate_start_value, line.gate_width_value, line.x_coordinate, line.y_coordinate, line.voltage_data, line.measurement_thickness, line.units])   # writing rows into the csv file 
                    
                value_matrix = []

                if y_movement == max(range(int(length_impulses)+1)):
                    #save_csv_file_func(value_matrix, scan_name)  # writes the data to a csv file
                    print('scan done')
                    operation_flag = 3
        
            GPIO.cleanup() 