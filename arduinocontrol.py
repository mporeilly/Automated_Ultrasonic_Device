#!/usr/bin/python3 
#https://www.youtube.com/watch?v=3QSsnnbJYFc&ab_channel=ElitheComputerGuy
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)