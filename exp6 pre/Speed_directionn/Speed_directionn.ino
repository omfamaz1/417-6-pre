// L298N H-Bridge Motor Control

// Pin Definitions for L298N
#define ENA 9    // Enable A (PWM for speed)
#define IN1 7    // Input 1
#define IN2 6    // Input 2

void setup() {
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  
  Serial.begin(9600);
  Serial.println("L298N Motor Control Ready");
}

void loop() {
  // Example sequence
  
  // Forward at 50% speed
  motorControl(1, 128);
  delay(2000);
  
  // Forward at 100% speed
  motorControl(1, 255);
  delay(2000);
  
  // Brake
  motorControl(0, 0);
  delay(1000);
  
  // Reverse at 75% speed
  motorControl(-1, 192);
  delay(2000);
  
  // Stop
  motorControl(0, 0);
  delay(2000);
}

void motorControl(int direction, int speed) {
  // direction: 1 = forward, -1 = reverse, 0 = stop/brake
  // speed: 0-255
  
  analogWrite(ENA, speed);
  
  if (direction == 1) {
    // Forward
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    Serial.println("Forward");
  } 
  else if (direction == -1) {
    // Reverse
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    Serial.println("Reverse");
  } 
  else {
    // Stop/Brake
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    Serial.println("Stop");
  }
  
  Serial.print("Speed: ");
  Serial.println(speed);
}