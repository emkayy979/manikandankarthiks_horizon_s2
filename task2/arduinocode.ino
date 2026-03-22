#include <Servo.h>

Servo s1; 
int pin = A0;   // knob at a0
int led = 13;   // led at 13
int degree;     

void setup() {
  s1.attach(9);        // motor at 9
  pinMode(led, OUTPUT); // led output
}

void loop() {
  int reading = analogRead(pin); // knob reading
  degree = map(reading, 0, 1023, 0, 180); // convert to degrees

  if (degree > 68) {
    s1.write(68);       // force stop at 68
    digitalWrite(led, HIGH); // led on
  } 
  else {
    s1.write(degree);   // move normally
    digitalWrite(led, LOW); // led off
  }

  delay(15); 
}