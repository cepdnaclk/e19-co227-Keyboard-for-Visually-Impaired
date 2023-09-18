#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

char handshake[50];

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming line of text terminated by a newline character
    Serial.readBytesUntil('\n', handshake, sizeof(handshake));
    
    // Print the received line of text
    Serial.print("Received: ");
    Serial.println(handshake);

    // Compare the received text with the SERVICE_UUID
    if (strcmp(handshake, SERVICE_UUID) == 0) {
      Serial.println(CHARACTERISTIC_UUID);
    }
  }
}
