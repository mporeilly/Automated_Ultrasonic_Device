def scan_voltage():
  #https://github.com/tmckay1/pi_read_analog/blob/master/potentiometer.py
  import busio
  import digitalio
  import board
  import adafruit_mcp3xxx.mcp3008 as MCP
  import time
  import RPi.GPIO as GPIO
  from adafruit_mcp3xxx.analog_in import AnalogIn

  ### add in popup window that displays the print statements
  # scan_window = tk.Tk()                                          # root is the window similar to index.html
  # scan_window.title('Calibration')                                # header info
  # scan_window.geometry('424x150')
  # width_label = tk.Label(root, text='Scan Width:')
  # width_label.grid(row=5, column=0)

  spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
  cs = digitalio.DigitalInOut(board.D5)
  mcp = MCP.MCP3008(spi, cs)
  channel = AnalogIn(mcp, MCP.P0)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(17,  GPIO.OUT)

  return str(channel.voltage)

  # while True:
  #   print('Raw ADC Value: ', channel.value)
  #   print('ADC Voltage: ' + str(channel.voltage) + 'V')
  #   time.sleep(0.5)

    ### updating video found https://www.youtube.com/watch?v=oZhJDDSUSRI&ab_channel=OnlineWebcoach
  # scan_window.mainloop()