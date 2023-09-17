#include <WiFi.h>

char x[] = "The Seriol Input"; // Define a character array (string)
char ssid[50];        // Buffer to store SSID
char password[50];    // Buffer to store password
char host[50];        // Buffer to store host IP
int currentCharIndex = 0;

void setup() {
  Serial.begin(9600); // Initialize serial communication with a baud rate of 9600
  delay(10);

  while (!Serial.available()) {
    // Wait for user input
  }
  Serial.readBytesUntil('\n', ssid, sizeof(ssid));

  while (!Serial.available()) {
    // Wait for user input
  }
  Serial.readBytesUntil('\n', password, sizeof(password));

  while (!Serial.available()) {
    // Wait for user input
  }
  Serial.readBytesUntil('\n', host, sizeof(host));

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    if (client.connect(host, 8888)) { // Change the port
      if (currentCharIndex < strlen(x)) {
        char currentChar = x[currentCharIndex];
        Serial.println(currentChar);
        client.print(currentChar); // Print the current character
        client.stop();
        currentCharIndex++;
        delay(1000); // 1 second delay between characters
      }
    }
  }
}
