#include <BluetoothSerial.h>

BluetoothSerial SerialBT; // Create a BluetoothSerial object

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_BT_Serial"); // Initialize Bluetooth with a unique name
}

void loop() {
  Serial.println("A");     // Send the character over Bluetooth
  delay(1000);
}
