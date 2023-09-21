# Author : Dasun Theekshana, Ravindu
# Date : 19/09/2023
# File : SerialReader.py

import asyncio
#from modulefinder import AddPackagePath
#from pkgutil import get_loader
#from site import addpackage

from src.SerialReader import *
from src.BluetoothReader import *
from src.WifiReader import *
from src.KeyBoard import *

mode = 1
agent = None

if __name__ == "__main__":
    def run():
        global agent
        agent.connect()
        while True:
            data = agent.read()
            if data:
                print(data)
                #keyboard.keypress(data)
                
    async def runbluetooth():
        global agent
        await agent.connect()
        while True:
            data = await agent.read()
            if data:
                print(data)
                #keyboard.keypress(data)
                
    #keyboard = KeyBoard()
    
    if mode == 0:
        agent = ESPSerialReader()
        run()
    elif mode == 1:
        agent = ESPBluetoothReader()
        asyncio.run(runbluetooth())
    elif mode == 2:
        agent = ESPWifiReader("0.0.0.0")
        run()