# Author : Dasun Theekshana
# Date : 19/09/2023
# File : SerialReader.py

import asyncio
from bleak import BleakScanner, BleakClient

service_uuid = '4fafc201-1fb5-459e-8fcc-c5c9c331914b'  # Service UUID
characteristic_uuid = 'beb5483e-36e1-4688-b7f5-ea07361b26a8' # Characteristic UUID

class ESPBluetoothReader:
    def __init__(self):
        self.macaddrs = None
        self.name = None
        self.devices = None
        self.client = None
        
    async def scan(self):
        self.devices = await BleakScanner.discover(return_adv=True)
        for device,data in self.devices.items():
            print(f"Name: {data[1].local_name} MAC: {device} RSSI: {data[1].rssi}")
            
    async def isavalable(self):
        await self.scan()
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
        if await self.isavalable():
            self.client = BleakClient(self.macaddrs)
            try:
                await self.client.connect()
                print(f"Connected to {self.name}")
                return True
                
            except Exception as e:
                print(f"Error Connecting: {str(e)}")
                return False
                
    async def disconnect(self):
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
        try:
            data = await self.client.read_gatt_char(characteristic_uuid)
            if data:
                return data.decode('utf-8')
            return False
        except Exception as e:
                print(f"Error Reading: {str(e)}")
                return False