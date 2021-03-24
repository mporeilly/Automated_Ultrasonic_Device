#!/usr/bin/python3 
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=5) 
# read from Arduino
input = ser.read()
print("Read input " + input.decode("utf-8") + " from Arduino")