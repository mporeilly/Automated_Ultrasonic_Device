def movescanner(radius, degrees, distance, direction):
    import math
    import time
    import RPi.GPIO as GPIO

    # if direction == "forward":
    #     direction = int(1)  # clockwise/forward (direction pin high)
    #
    # else:
    #     direction = int(0)  # counterclockwise/reverse (direction pin low)

    step_angle = degrees
    m_pins = (10, 12, 32)  # M-pins of driver set to GPIO pins 10 12 and 32 on pi
    # step = 23  # step pin of driver set to GPIO 23 on pi
    # dir = 24  # dir pin of driver set to GPIO 24 on pi
    step = 21  # step pin of driver set to GPIO 23 on pi
    dir = 20
    half = (1, 0, 0)  # sequence of m-pins activation for half stepping (M0 high, M1 and M2 low)

    # Note that may be able to just pull the M-pins high and low by connecting M0 to 3.3v rail, M1 and M2 to ground
    # rather than using GPIO pins. Will test both

    GPIO.setmode(GPIO.BCM)  # Sets pin naming convention
    GPIO.setup(dir, GPIO.OUT)  # setting the direction, step, and resolution pins as outputs
    GPIO.setup(step, GPIO.OUT)
    GPIO.setup(m_pins, GPIO.OUT)

    GPIO.output(dir, direction)  # sets dir pin high or low based on direction that it is passed (forward/reverse)
    GPIO.output(m_pins, half)  # sets half step mode (M0 high, M1 and M2 low)

    counter = 0
    maximum = int(distance / (step_angle * ((2 * math.pi) / 360) * radius))  # determines half steps to travel distance

    # for steps in range(maximum):  # looping through maximum number of half step pulses
    GPIO.output(step, GPIO.HIGH)  # step pin set high
    time.sleep(0.01)  # delay between pulses (test different values)
    GPIO.output(step, GPIO.LOW)  # step pin set low
    time.sleep(0.01)  # delay between pulses (test different values)

    go = 1
    return go  # once wheels have moved desired distance, the return value initiates the next function call in main file