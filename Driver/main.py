import asyncio
from modulefinder import AddPackagePath
from pkgutil import get_loader
from site import addpackage
import pynput.keyboard as keyboard

from src.SerialReader import *
from src.BluetoothReader import *
from src.WifiReader import *

mode = 1
agent = None

k = keyboard.Controller()

def send_char_to_input_buffer(c):
    """Sends a character to the keyboard input buffer."""
    k.press(c)
    k.release(c)

if __name__ == "__main__":
    def run():
        global agent
        agent.connect()
        while True:
            data = agent.read()
            if data:
                print(data)
                send_char_to_input_buffer(data)
                
    async def runbluetooth():
        global agent
        agent = ESPBluetoothReader()
        await agent.connect()
        while True:
            data = await agent.read()
            if data:
                print(data)
                send_char_to_input_buffer(data)
       
    if mode == 0:
        agent = ESPSerialReader()
        agent.connect()
        run()
    elif mode == 1:
        asyncio.run(runbluetooth())
    elif mode == 2:
        agent = ESPWifiReader("0.0.0.0")
        run()
    """
    agent = ESPSerialReader()
    agent.connect()
    while True:
            data = agent.read()
            if data:
                print(data)
    
    """
