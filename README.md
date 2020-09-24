# capstone
The files within this repo will hold the software for an automated UT device that is designed to complete API 563 tank inspections. The device will be used to follow up on MFL tools to provide quantitative records. The UT scanner will prevent manual inspection and increase the coverage area with data saved to excel style files providing a heat map of the area inspected.
The design will include the scanning in the X direction along driving in the Y axis to cover the designated area. Two stepper motors will be used to control the movement in the two directions. The controller will be a raspberrypi, this was chosen over an Arduino due to the ability to natively write out files to an USB drive. 
