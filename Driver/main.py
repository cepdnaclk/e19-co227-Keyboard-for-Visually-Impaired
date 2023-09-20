import asyncio
from modulefinder import AddPackagePath
from pkgutil import get_loader
from site import addpackage

from src.SerialReader import *
from src.BluetoothReader import *
from src.WifiReader import *

mode = 0
agent = None

if __name__ == "__main__":
    def run():
        global agent
        agent.connect()
        while True:
            data = agent.read()
            if data:
                print(data)
                
    async def runbluetooth():
        global agent
        agent = ESPBluetoothReader()
        await agent.connect()
        while True:
            data = await agent.read()
            if data:
                print(data)
    """        
    if mode == 0:
        agent = ESPSerialReader()
        agent.connect()
    elif mode == 1:
        asyncio.run(runbluetooth())
    elif mode == 2:
        agent = ESPWifiReader("0.0.0.0")
        run()"""
    agent = ESPSerialReader()
    agent.connect()
    

