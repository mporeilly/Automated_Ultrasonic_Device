def scan_voltage(ser):
#https://www.youtube.com/watch?v=3QSsnnbJYFc&ab_channel=ElitheComputerGuy
  voltage = ser.readline().decode('utf-8').rstrip()
  return str(voltage)