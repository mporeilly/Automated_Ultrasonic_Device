def scan_voltage():
  #https://github.com/tmckay1/pi_read_analog/blob/master/potentiometer.py
  import busio
  import digitalio
  import board
  import adafruit_mcp3xxx.mcp3008 as MCP
  import time
  import RPi.GPIO as GPIO
  from adafruit_mcp3xxx.analog_in import AnalogIn

  spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
  cs = digitalio.DigitalInOut(board.D5)
  mcp = MCP.MCP3008(spi, cs)
  channel = AnalogIn(mcp, MCP.P0)

  return str(channel.voltage)