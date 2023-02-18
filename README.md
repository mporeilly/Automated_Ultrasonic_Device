# Capstone
The files within this repository contain software used to control an Automated Ultrasonic Device that is designed to complete API 563 tank inspections. The software was designed around a Raspberry Pi and Olympus UT scopes capable of outputting scan data as analog voltage signals between 0 - 1 Volt. Due to interference from the GPIO pins on the Pi an Arduino will collect the voltage values. The values will then be sent to the Pi over a serial connection via a USB cable. Please refer to the wiring diagram below for the setup.


![alt text](https://github.com/mporeilly/Capstone/blob/master/Electrical/Schematic_Wiring%20Diagram.png)


  
INSTALL INSTRUCTIONS
----------------   
  
1. Download the GitHub repo to the Raspberry PI
2. Navigate into the downloaded folder in a terminal application
3. Create a virtual python environment 
   >python3 -m venv venv_utapp
4. Activate the virtual environment
   >source venv_utapp/bin/activate
5. Edit the permissions of the setup.sh file 
   >chmod 775 setup.sh
6. Run the setup script 
   >sudo ./setup.sh
7. Download the Arduino application from the offical site: https://www.arduino.cc/en/software
8. Plug in the Arduino to the Raspberry Pi with a USB A to B cable
9. Open the Arduino application and upload **voltagecollector.ino** from the arduino folder within the Capstone folder (Edit the parameters to meet voltage levels from scope output)


Running the Application
--------------

1. Navigate to the folder location in a terminal application
2. Activate the previously created virtual environment
   >source venv_utapp/bin/activate
3. Now start the program
   >python main.py


![alt text](https://github.com/mporeilly/Capstone/blob/master/Photos/GUI_V2.png)


Install Touch Keyboard
--------
   
The software setup steps found https://pimylifeup.com/raspberry-pi-on-screen-keyboard/

Solution to "Errno [24]"
---------
1. Run the command 
    >ulimit -Hn
2. Run the command below, the value returned here seems to be the system's limit 
    >ulimit -Sn  
3. Edit config file 
    >sudo nano /etc/security/limits.conf
4. Add a line to the file 
    >\* soft nofile 50000
  
Sources:
  
  https://www.24x7serversupport.com/blog/how-to-increase-the-ulimit-and-file-descriptors-limit-in-linux/
  https://www.tecmint.com/increase-set-open-file-limits-in-linux/
