// Pin number for the built-in LED on the ESP32
const int ledPin = 2; // GPIO 2

void setup() {
  // Initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Turn the LED on (HIGH)
  digitalWrite(ledPin, HIGH);

  // Wait for 500 milliseconds (0.5 seconds)
  delay(500);

  // Turn the LED off (LOW)
  digitalWrite(ledPin, LOW);

  // Wait for 500 milliseconds (0.5 seconds)
  delay(500);
}
