# Author : Dasun Theekshana, Ravindu Abeysinghe
# Date : 19/09/2023
# File : SerialReader.py

import asyncio
from bleak import BleakScanner, BleakClient

# Define the service UUID and characteristic UUID for the BLE device

service_uuid = '4fafc201-1fb5-459e-8fcc-c5c9c331914b' 
characteristic_uuid = 'beb5483e-36e1-4688-b7f5-ea07361b26a8' 

class ESPBluetoothReader:
    def __init__(self):
        self.macaddrs = None      # Stores the MAC address of the selected BLE device
        self.name = None          # Stores the name of the selected BLE device
        self.devices = None       # Stores discovered BLE devices
        self.client = None        # Stores the BleakClient object for the selected device
        
    async def scan(self):
        """
        Discover nearby BLE devices and return their advertising data.
        """
        try:
            self.devices = await BleakScanner.discover(return_adv=True)
            for device,data in self.devices.items():
                print(f"Name: {data[1].local_name} MAC: {device} RSSI: {data[1].rssi}")
        except Exception as e:
            print(f"Error Turn On Bluetooth: {str(e)}")
            
    async def isavalable(self):
        """
        Check if the desired BLE device is available.
        """
        await self.scan()    # Perform a scan to discover devices
        if self.devices:
            devicename = input("Enter the Devices Name: ")
            for device,data in self.devices.items():
                name = data[1].local_name
                if devicename == name:
                    self.macaddrs = device
                    self.name = name
                    return True
        print("Device not Found")
        return False
    
    async def connect(self):
        """
        Connect to the selected BLE device.
        """
        if await self.isavalable():
            # Create a BleakClient instance for the selected device
            self.client = BleakClient(self.macaddrs)
            try:
                # Connect to the selected BLE device
                await self.client.connect()
                print(f"Connected to {self.name}")
                return True
                
            except Exception as e:
                print(f"Error Connecting: {str(e)}")
                return False
        return True
                
    async def disconnect(self):
        """
        Disconnect from the selected BLE device.
        """
        try:
            await self.client.disconnect()
            print(f"{self.name} disonnected")
            self.name = None
            self.macaddrs = None
            self.client = None
            return True
        except Exception as e:
                print(f"Error Disonnecting: {str(e)}")
                return False
    
    async def read(self):
        """
        Read data from the specified BLE characteristic.
        """
        try:
            data = await self.client.read_gatt_char(characteristic_uuid)
            if data:
                return data.decode('utf-8')
            return False
        except Exception as e:
                print(f"Error Reading: {str(e)}")
                return False

# Example usage:
# reader = ESPBluetoothReader()
# await reader.connect()
# data = await reader.read()
# await reader.disconnect()
