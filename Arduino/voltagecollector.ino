//https://www.youtube.com/watch?v=_H16GYL08Ik&ab_channel=ProgrammingElectronicsAcademy
void setup(){
  Serial.begin(9600); // this is the baud rate 
}

void loop(){
  // read the input on the analog pin 0
  int sensorValue = analogRead(A0);

  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0-1v)
  float voltage = sensorValue * (1.000 / 1023);
  // print out the voltage value to the serial interface to 4 decimal places
  Serial.println(voltage, 4); // this means print to 4 digits after the decimal
  delay(50);
  
  
}
