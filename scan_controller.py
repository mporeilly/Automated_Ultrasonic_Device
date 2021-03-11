import math
import time
from WheelStepperFunction import movewheels  # importing created functions from external files
from TransducerStepperFunction import movescanner
from analogtodig import scan_voltage
from csv_function_file import save_csv_file_func
#import RPi.GPIO as GPIO

def scan_control(width, length, gate_start, gate_width, unit, operation_flag, scan_name):
    # if statement to make sure the values fit within the
    value_matrix = [] # initalizing the array that will hold the DataPoint values


    # zeroing of the transducter 
    # while True:
    # move transducter direction 
    # if gpio pin 17 == HIGH:
    #   False


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

    # linear interpolation to get the correct thickness from the voltage collected
    def interpolation_func(voltage, gate_start, gate_width):
        thickness = (((voltage*(gate_start+gate_width)-gate_start))/(1))+gate_start
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
                print(str(y_movement) + ' is y move and width_impulses is ' + str(x_movement)) 
                
                # if gpiopins is high:
                #     return    # this will stop the machine from moving when the emergency stop is activated
                voltage = scan_voltage()
                thickness = interpolation_func(voltage, gate_start, gate_width)
                # https://www.youtube.com/watch?v=Ercd-Ip5PfQ&ab_channel=CoreySchafer
                x_coordinate = impulse_to_measurement(x_movement)                           # need to account for the path back
                y_coordinate = impulse_to_measurement(y_movement)       
                value_matrix.append(DataPoint(scan_name, gate_start, gate_width, x_coordinate, y_coordinate, voltage, thickness, unit_text))
      
            if y_movement == max(range(int(length_impulses)+1)):
                save_csv_file_func(value_matrix, scan_name)  # writes the data to a csv file
                print('scan done')
                operation_flag = 3

        