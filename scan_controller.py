def scan_control(width, length, gate_start, gate_width, unit, operation_flag, scan_name):
    print('enter control func')
    print(unit)
    # if statement to make sure the values fit within the
    import math
    import time
    from WheelStepperFunction import movewheels  # importing created functions from external files
    from TransducerStepperFunction import movescanner


    if unit != 1 and unit != 2:
        return

    if unit == 2:
        radius = 1.5  # wheel radius in inches
        belt = 1  # temporary belt radius in inches
        yincrement = 0.75  # y increment in inches
    if unit == 1:
        radius = 38.1  # wheel radius in mm
        belt = 25.4  # temporary belt radius in mm
        yincrement = 19.05  # y increment in mm

    scanPath = width  # length of scanner path
    degrees = 1.8/2  # degrees per step (for full stepping, half stepping is utilized in the move functions)
    stepincrement = int(yincrement / (degrees * ((2 * math.pi) / 360) * radius))  # number of steps in y increment

    # linear interpolation to get the correct thickness from the voltage collected
    def interpolation_func(voltage, gate_start, gate_width):
        thickness = (((voltage*(gate_start+gate_width)-gate_start))/(1))+gate_start
        return thickness


    def measurement_to_impulse(length,unit):
        #returns the number of impulses required to drive the
        impulse_number = int(float(length) / (degrees * ((2 * math.pi) / 360) * radius)) # steps per length
        return impulse_number

    def voltage_collector():
        print('voltage collector activated')

        ###

        # need to introduce the analogtodigital into this file and the associated imports

        return voltage


    length_impulses = measurement_to_impulse(length, unit) / stepincrement # number of forward increments in grid
    width_impulses = measurement_to_impulse(length,unit)  # number of steps per probe sweep
    xdirection = 1  # starting direction of probe set to left->right
    ydirection = 1  # starting direction of wheels set to forward
    ximpulses = 0 # variable for counting impulses to determine direction (odd impulses = left->right, vise versa)
    yimpulses = 0 # variable for counting impulses to determine direction (odd impulses = forward, vise versa)
    print(range(int(length_impulses)))


    print('op flag value ' + str(operation_flag))
    while operation_flag == 1: # this is for the emergency stop to be wired to

        
        for y_movement in range(int(length_impulses)):
            #time.sleep(1)
            print('y move '+ str(y_movement))
            
            movewheels(radius, degrees, yincrement, ydirection)

            print('in first for loop')
            if y_movement == length_impulses:  # when length is reached, reverse wheel direction
                ydirection = 0

            if y_movement % 2 != 0:  # this reverses x direction after each probe sweep
                xdirection = 0
            else:
                xdirection = 1

            for x_movement in range(int(width_impulses)):
                print(' trans loop max '+ str(int(length_impulses)))
                if y_movement >= (int(length_impulses)-1):
                    print('the opertaion flag was hit in trans loop')
                    operation_flag = 0
                    break

                print('x move '+ str(x_movement))
                
                # if gpiopins is high:
                #     operation_flag = 0    # this will stop the machine from moving when the emergency stop is activated
                #voltage = voltage_collector()
                #thickness = interpolation_func(voltage, gate_start, gate_width)
                # https://www.youtube.com/watch?v=Ercd-Ip5PfQ&ab_channel=CoreySchafer
                print('in transducer loop')
                movescanner(belt, degrees, width_impulses, xdirection)
            if operation_flag == 0:
                print('operation if statement hit in wheel loop')
                break

                print(x_movement)
                
            
                
                


