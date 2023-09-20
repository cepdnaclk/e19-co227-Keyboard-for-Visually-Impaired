#include <WiFi.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

char ssid[50];      // Buffer ro store SSID   
char password[50];  // Buffer to store password
char host[50];      // Buffer to store host IP

int port = 8888;     // Port to Connect
int mode;           // Mode connect with PC

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristic= NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;
uint32_t value = 0;

class MyServerCallbacks: public BLEServerCallbacks{
  void onConnect(BLEServer* pServer){
    deviceConnected = true;
    Serial.println("Connected");
  };

  void onDisconnect(BLEServer* pServer){
    deviceConnected = false;
    Serial.println("Disconnected");
  }
};

void setup() {
  Serial.begin(9600);
  Serial.println();

  getmode();
  // mode = 1;
  if (mode == 0){
    Serial.println("USB");
  }else if (mode == 1){
    Serial.println("Bluetooth");
    connectBluetooth();
  }else if (mode == 2){
    Serial.println("WiFi");
    // getWiFiCredential();
    // connectWiFi();
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (mode == 0){
    Serial.println('A');
  }else if (mode == 1){
    sendBluetooth('A');
  }else if (mode == 2){
    // sendWiFi('A');
  }
  delay(300);

}

void getmode(){
  Serial.println("Mode:");
  while(!Serial.available()){} // Wait for ussid
  mode = Serial.parseInt();
  Serial.readBytesUntil('\n', ssid, sizeof(ssid));
}

void getWiFiCredential(){
  Serial.println("SSID:");
  while(!Serial.available()){} // Wait for ussid
  Serial.readBytesUntil('\n', ssid, sizeof(ssid));

  Serial.println("Password:");
  while(!Serial.available()){} // Wait for password
  Serial.readBytesUntil('\n', password, sizeof(password));

  Serial.println("IP Address:");
  while(!Serial.available()){} // Wait for device IP
  Serial.readBytesUntil('\n', host, sizeof(host));
}

void connectWiFi(){
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi....");
  while (WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print("..");
  }
  Serial.println(".");
  Serial.println("Connected to WiFi");
}

bool sendWiFi(char data){
  if (WiFi.status() == WL_CONNECTED){
    WiFiClient client;
    if (client.connect(host, port)){
      Serial.println(data); // TODO: Remove this. this is testing perpose only
      client.print(data); // Send data
      client.stop();
      return true;
    }
    return false;
  }
  return false;
}

void connectBluetooth(){
  // Create the BLE Device
  BLEDevice::init("ESP32");  

  // Create the BLE Server
  pServer = BLEDevice::createServer(); 
  pServer->setCallbacks(new MyServerCallbacks());

  //Create the BLE Service
  BLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Charateristic
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_WRITE  |
                      BLECharacteristic::PROPERTY_NOTIFY |
                      BLECharacteristic::PROPERTY_INDICATE 
                    );

  // Create a BLE Descriptor
  pCharacteristic->addDescriptor(new BLE2902());

  // Start he service
  pService->start();

  // Start Advertising
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID); 
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);
  BLEDevice::startAdvertising();
  Serial.println("Waiting a client connection to notify...");
}

bool sendBluetooth(char data){
  // Notify changed data
  if (deviceConnected){
    pCharacteristic->setValue((uint8_t*)&data, 1);
    Serial.println(data); // TODO: Remove this. this is testing perpose only
    pCharacteristic->notify();
    return true;
    //delay(300); // TODO:To avoid congestion
  }
  return false;
}

void bluetoothReconect(){
  pServer->startAdvertising(); // Restart advertising
  Serial.println("start advertising");
}
