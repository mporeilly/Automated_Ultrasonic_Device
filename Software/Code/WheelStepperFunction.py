def movewheels(radius, degrees, distance, outpins, direction):

    import math
    import time
    # Import RPi.GPIO

    forwardsequence = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0],
                       [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]
    backwardsequence = [[1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0],
                        [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

    if direction == "forward":
        sequence = forwardsequence
    else:
        sequence = backwardsequence
    step_angle = degrees/2
    # steps_per_rev = (360/degrees)*2  # should equal 400 with nema17 dual shaft, 1.8deg step angle
    # move_angle = (distance/radius)*360/(2*math.pi)
    # steps = round(move_angle/step_angle)
    # cycles = steps/8

    # note that the smallest angle we can resolve is 0.9deg or 0.015708rads, this limits our distance precision
    # smaller wheel radius will be best for resolving smaller distances / come closer to target specified distances
    counter = 0
    while counter < distance:  # moves wheels until another step would exceed desired distance
        for step in range(8):  # looping through half steps
            for pin in range(4):  # looping through the pins 1 to 4 (index 0 to 3 of the list)
                if counter >= distance:
                    break
                GPIO.output(outpins[pin], sequence[step][pin])  # Sets each pin output in sequence, library command
                time.sleep(0.001)  # time delay otherwise pins energized too fast
            counter = counter + (step_angle * ((2 * math.pi) / 360) * radius)
            if counter >= distance:
                break
    go = 1
    return go
