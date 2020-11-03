# Capstone
The files within this repository will hold the software for an automated UT device that is designed to complete API 563 tank inspections. The device will be used to follow up on MFL tools to provide quantitative records. The UT scanner will prevent manual inspection and increase the coverage area with data saved to excel style files providing a heat map of the area inspected.

The design will include the scanning in the X direction along driving in the Y axis to cover the designated area. Two stepper motors will be used to control the movement of the tool in two directions. The controller will be a Raspberrypi, this was chosen over an Arduino due to the ability to natively write out files to an USB drive. A touch screen will be used to display a heatmap of the inspected area to the operator in real time. The displacement of the machine will be measured by a rotary encoder. The encoder will be intependent of the drive wheels to allow accurate measurements even if the drive wheels slip.

The programming language used will be Python due to the connections already rooted in the Raspberry Pi operating system and the ease of use.

The full documentation will include:
  - Wiring Schematics
  - Component Model Numbers and Spec Sheets
  - CAD Model
  - Bill of Materials
  - Software 
  
  
  
  INSTALL INSTRUCTIONS (Building the frame work to allow this to be the only steps needed to update a stock Raspberrypi) (Will look to put a package together so unneccissary files are excluded from the download)
1. $ apt install python3
2. $ apt install python3-pip
3. $ cd /home/pi/Desktop/
4. $ mkdir scanner
5. $ cd scanner
6. $ wget https://github.com/...
7. $ unzip master.zip
8. $ pip3 install -r requirements.txt

