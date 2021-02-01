def scan_control(width, length, gate_start, gate_width, unit, operation_flag):

    # if statement to make sure the values fit within the 
    if unit != 1 or unit != 2:
        return

    # linear interpolation to get the correct thickness from the voltage collected
    def interpolation_func(voltage, gate_start, gate_width):
        thickness = (((voltage*(gate_start+gate_width)-gate_start))/(1))+gate_start
        return thickness


    def measurement_to_impulse(length,unit):
        #returns the number of impulses required to drive the
        if unit == 1: # this is the milimeter case
            print('milimeter calculation function activated')
            return impulse_number
            
        if unit == 2: # this is the milimeter case
            print('inch calculation function activated')
            return impulse_number


    def voltage_collector():
        print('voltage collector activated')

        ###

        # need to introduce the analogtodigital into this file and the associated imports

        return voltage



    while operation_flag == 1: # this is for the emergency stop to be wired to


        length_impulses = measurement_to_impulse(length,unit)
        width_impulses = measurement_to_impulse(length,unit)

        for x_movement in length_impulses:
                
            print(x_movement)

            for y_movement in width_impulses:              
                # if gpiopins is high:
                #     operation_flag = 0    # this will stop the machine from moving when the emegency stop is activated
                voltage = voltage_collector()
                thickness = interpolation_func(voltage, gate_start, gate_width)
                # https://www.youtube.com/watch?v=Ercd-Ip5PfQ&ab_channel=CoreySchafer
                print(y_movement)

