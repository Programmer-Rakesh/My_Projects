#include <Servo.h>

Servo servo1, servo2, servo3;

void setup() {
    servo1.attach(9);
    servo2.attach(10);
    servo3.attach(11);
}

void loop() {
    
    servo1.write(50);
    delay(300);
    servo2.write(30);
    servo3.write(5);
    delay(300); 
  
    servo1.write(0);
    delay(300);
    servo2.write(0);
    servo3.write(25);
    
    delay(300); 
}
