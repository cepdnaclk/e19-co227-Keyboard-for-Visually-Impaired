// Author : Lahiru Manikdiwela, Harith Abeysinghe, Dasun Theekshana
// File : KeyBoard.ino
// Date : 19/09/2023

#include <WiFi.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include <array>

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

// Selected Pinn of the ESP32
const int button_0 = 17;
const int button_1= 18;
const int button_2 = 19;
const int button_3 = 21;
const int button_4 = 25;
const int button_5= 26;
const int button_6 = 27;
const int button_7 = 32;
const int button_8 = 33;

char ssid[50];      // Buffer ro store SSID   
char password[50];  // Buffer to store password
char host[50];      // Buffer to store host IP
String modec = "";

int port = 8888;     // Port to Connect
int mode;           // Mode connect with PC
int arr[9]= {0, 0, 0, 0, 0, 0, 0, 0, 0};
int encodeButtons(int arr[], int size){
    int code = 0;
    for (int i=0; i<size; i++){
        code += (1<<i)*arr[i];

    }
    return code;
}


//int test[] = {1, 17, 0, 8, 11, 4, -3, 19, 4, 18, 19, -4, 1, -3, -4, 0, 18};

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

//   //Serial.println();
//  Initilizing the Mode of the Pins
//   Serial.println("h");
  pinMode(button_0, INPUT);
  pinMode(button_1, INPUT);
  pinMode(button_2, INPUT);
  pinMode(button_3, INPUT);
  pinMode(button_4, INPUT);
  pinMode(button_5, INPUT);
  pinMode(button_6, INPUT);
  pinMode(button_7, INPUT);
  pinMode(button_8, INPUT);


  getmode();
  // mode = 1;
  if (mode == 48){
    Serial.println("USB");
  }else if (mode == 49){
    Serial.println("Bluetooth");
    //connectBluetooth();
  }else if (mode == 50){
    Serial.println("WiFi");
    getWiFiCredential();
    connectWiFi();
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (mode == 48){
    //Serial.println(5);
    for (int i =0;i<14;i++){
      Serial.println(test[i]);
      delay(1000);
    }
  }else if (mode == 49){
    //sendBluetooth('A');
  }else if (mode == 50){
    //sendWiFi(5);
     for (int i =0;i<14;i++){
      sendWiFi(test[i]);
      delay(1000);
    }
  }

  // Reading States of all the Pins
  arr[0] = digitalRead(button_0);
  arr[1] = digitalRead(button_1);
  arr[2] = digitalRead(button_2);
  arr[3] = digitalRead(button_3);
  arr[4] = digitalRead(button_4);
  arr[5] = digitalRead(button_5);
  arr[6] = digitalRead(button_6);
  arr[7] = digitalRead(button_7);
  arr[8] = digitalRead(button_8);
  
  // arr[0]= 0;
  // arr[1] = 1;
  // arr[2] = 1;
  delay(500);
  int encoded = encodeButtons(arr, 8);
  Serial.println(encoded);
  // Serial.println(arr[2]);

  delay(3000);

}

void getmode(){
  Serial.println("Mode:");
  while(!Serial.available()){} // Wait for ussid
  modec = Serial.read();
  Serial.readBytesUntil('\n', ssid, sizeof(ssid));
  mode = modec.toInt();
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

bool sendWiFi(int data){
  if (WiFi.status() == WL_CONNECTED){
    WiFiClient client;
    if (client.connect(host, port)){
      Serial.println(data); // TODO: Remove this. this is testing perpose only
      client.println(data); // Send data
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

bool sendBluetooth(int data){
  // Notify changed data
  if (deviceConnected){
    pCharacteristic->setValue((uint8_t*)&data, 1);
    Serial.println(data); // TODO: Remove this. this is testing perpose only
    pCharacteristic->notify();
    return true;
    delay(300); // TODO:To avoid congestion
  }
  return false;
}

void bluetoothReconect(){
  pServer->startAdvertising(); // Restart advertising
  Serial.println("start advertising");
}
