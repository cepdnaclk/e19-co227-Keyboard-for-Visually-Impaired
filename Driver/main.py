# Author : Dasun Theekshana, Ravindu Abeysinghe
# Date : 19/09/2023
# File : main.py

import asyncio
import threading
#from modulefinder import AddPackagePath
#from pkgutil import get_loader
#from site import addpackage

from src.SerialReader import *
from src.BluetoothReader import *
from src.WifiReader import *
from src.KeyBoard import *
from src.KeyDecoder import *
from src.GUI import *

mode = 0
agent = None

if __name__ == "__main__":
    def run():
        global agent
        agent.connect()
        while True:
            data = agent.read()
            if data:
                #print(data)
                letter = decoder.decode(int(data))
                if letter:
                    print(letter)
                    #keyboard.keypress(data)
                
    async def runbluetooth():
        global agent
        await agent.connect()
        while True:
            data = await agent.read()
            if data:
                print(data)
                #keyboard.keypress(data)

    def set_mode(new_mode):
        global mode, agent
        mode = new_mode
        
        if agent:
            agent = None
        if mode == 0:
            agent = ESPSerialReader()
            #run()
        elif mode == 1:
            agent = ESPBluetoothReader()
            #asyncio.run(runbluetooth())
        elif mode == 2:
            agent = ESPWifiReader("0.0.0.0")
            #run()
        threading.Thread(target=run).start()
         
                
    #keyboard = KeyBoard()
    decoder = KeyDecoder()
    root = tk.Tk()
    
    gui = GUI(root, set_mode)
    root.mainloop()
    