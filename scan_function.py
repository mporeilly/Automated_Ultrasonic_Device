def scan_func(width):# , length, thick_max, thick_min, unit )
 
    from WheelStepperFunction import movewheels  # importing created functions from external files
    from TransducerStepperFunction import movescanner
    radius = 1  # temporary wheel radius
    belt = 1  # temporary belt radius
    scanPath = 12  # length of scanner path
    degrees = 1.8  # degrees per step (for full stepping, half stepping is utilized in the move functions)
    distance = 0.75  # desired forward distance per scan, in inches (could make this a user input with GUI)
    count = 0  # counts number of scans, used for while-loop exit condition



    # linear interpolation to get the correct thickness from the voltage collected
    def interpolation_func(voltage, gate_start, gate_width):
        thickness = (((voltage*(gate_start+gate_width)-gate_start))/(1))+gate_start
        return thickness

    go = 1
    direction = "forward"

    # forward scan loop
    while count < ((scanPath/distance)+1):  # (inches of grid to scan / distance per scan = number of scans) +1 at start    left right
        if go == 1:
            go = 0
            go = movescanner(belt, degrees, scanPath, direction)
            count += 1
        if go == 1:
            go = 0
            direction = "forward"
            go = movewheels(radius, degrees, distance, direction)               #forward back

            if count % 2 != 0:
                direction = "reverse"
            else:
                direction = "forward"

    go = 1
    direction = "reverse"
    # Implement/verify reverse to origin after forward scan is working
    # Reverse scan loop
    while count < (
            (12 / distance) + 1):  # (12 inches of grid to scan / distance per scan = number of scans) +1 scan at start
        if go == 1:
            go = 0
            go = movescanner(belt, degrees, scanPath, scannerOutpins, direction)
            count += 1
        if go == 1:
            go = 0
            direction = "reverse"
            go = movewheels(radius, degrees, distance, wheelOutpins, direction)

            if count % 2 != 0:
                direction = "forward"
            else:
                direction = "reverse"

# may have to play around with different time delays, optimize for speed/torque
# Causes device to inch forward in the y direction before scanning again in the x direction (serpentine scanning path)


    # should return data of the scan