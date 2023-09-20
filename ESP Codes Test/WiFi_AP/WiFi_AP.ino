#include <WiFi.h>

const char* ssid = "ESP32" ;
const char* password = "123456789";

WiFiServer server(8888);

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  server.begin();


}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client = server.available();

  if (client){
    while (client.connected()){
      if (client.available()){
        client.println("A");
        Serial.println("A");
      }
    }
  }

  client.stop();

}
