# capstone
The files within this repository will hold the software for an automated UT device that is designed to complete API 563 tank inspections. The device will be used to follow up on MFL tools to provide quantitative records. The UT scanner will prevent manual inspection and increase the coverage area with data saved to excel style files providing a heat map of the area inspected.

The design will include the scanning in the X direction along driving in the Y axis to cover the designated area. Two stepper motors will be used to control the movement of the tool in two directions. The controller will be a Raspberrypi, this was chosen over an Arduino due to the ability to natively write out files to an USB drive. A touch screen will be used to display a heatmap of the inspected area to the operator in real time. The displacement of the machine will be measured by a rotary encoder. The encoder will be intependent of the drive wheels to allow accurate measurements even if the drive wheels slip.

The programming language used will be Python due to the connections already rooted in the Raspberrypi operating system and the ease of use.

The full documentation will include:
  - Wiring Schematics
  - Model number of the components used and their associated specs sheets
  - CAD models of the tool
  - Complete bill of materials
  - Software 
