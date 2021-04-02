# Capstone
The files within this repository contain software used to control an automated UT device that is designed to complete API 563 tank inspections. The software was designed around a Raspberry Pi and UT scopes capable of outputting scan data as analog voltage signals between 0 - 1 volt. Due to interference from the GPIO pins on the Pi an Arduino will take care of collecting the voltage values which will then be sent to the Pi over a serial connetion in the form of a USB cable. Please refer to the wiring diagram for setup of the wiring harness.


  
  INSTALL INSTRUCTIONS:
  ----------------   
  '''
1. $ Download the GitHub repo to the Raspberry PI
2. $ Navigate to the folder in the terminal application
3. $ Edit the permissions of the setup.sh file by typing "chmod 775 setup.sh"
4. $ Run the setup script by typing "sudo ./setup.sh"
5. $ To run the application by typing "python main.py"
'''


Install Touch Keyboard
   
    The software setup steps found https://pimylifeup.com/raspberry-pi-on-screen-keyboard/

Solution to "Errno [24]"

    run the command "ulimit -Hn"
    run the command "ulimit -Sn"  <- the value returned here seems to be the system's limit 
  
    edit a config file "sudo nano /etc/security/limits.conf"
    add a line to the file "* soft nofile 50000"
  
    Sources
  
     https://www.24x7serversupport.com/blog/how-to-increase-the-ulimit-and-file-descriptors-limit-in-linux/
     https://www.tecmint.com/increase-set-open-file-limits-in-linux/
