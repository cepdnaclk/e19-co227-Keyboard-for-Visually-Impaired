import asyncio
from bleak import BleakScanner, BleakClient

async def read_data_from_characteristic(device_address, service_uuid, characteristic_uuid):
    print("In function")
    #async with BleakClient(device_address) as client:
    client = BleakClient(device_address)
    try:
        await client.connect()
        print(f"Connected to {device_address}")
        while True:
            data = await client.read_gatt_char(characteristic_uuid)
            #print("Model Number: {0}".format("".join(map(chr, model_number))))
            #integer_value = int.from_bytes(data_bytes, byteorder='little')
           # print(f"Data: {integer_value}")
            if data:
                print(f"Data: {data.decode('utf-8')}")
            await asyncio.sleep(1)

        #services = await client.get_services()
        #for service in services:
            #print(service)        
            #if service.uuid == service_uuid:
                #characteristics = await service.get_characteristics()
                #for characteristic in characteristics:
                    #if characteristic.uuid == characteristic_uuid:
                        #while True:
                            #data = await client.read_gatt_char(characteristic.uuid)
                            #print(f"Data from {device_address}: {data.decode('utf-8')}")
                            #await asyncio.sleep(1)  # Adjust the delay as needed
    except Exception as e:
        print(f"Error reading data: {str(e)}")

async def main():
    characteristic_uuid = "beb5483e-36e1-4688-b7f5-ea07361b26a8"  # Replace with the UUID of the characteristic
    
    devices = await BleakScanner.discover(return_adv=True)
    
    for device,data in devices.items():
        print(data[1].local_name)
        print(device)
        print(data[1].service_uuids)
        print(data[1].rssi)
        print()
    
    await read_data_from_characteristic("0C:B8:15:C3:A8:EA","4fafc201-1fb5-459e-8fcc-c5c9c331914b", "beb5483e-36e1-4688-b7f5-ea07361b26a8")

asyncio.run(main())
"""

async def read_ble_characteristic(address, service_uuid, characteristic_uuid):
    async with BleakClient(address) as client:
        value = await client.read_gatt_char(characteristic_uuid)
        print(f'Received: {value.decode("utf-8")}')

address = '00:11:22:33:44:55'  # Replace with your device's MAC address
service_uuid = '0000XXXX-0000-1000-8000-00805f9b34fb'  # Replace with your service UUID
characteristic_uuid = '0000YYYY-0000-1000-8000-00805f9b34fb'  # Replace with your characteristic UUID

asyncio.run(read_ble_characteristic(address, service_uuid, characteristic_uuid))
"""