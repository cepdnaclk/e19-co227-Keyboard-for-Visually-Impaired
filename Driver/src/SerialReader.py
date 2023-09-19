# Author : Dasun Theekshana
# Date : 19/09/2023
# File : SerialReader.py

import serial
import serial.tools.list_ports

class ESPSerialReader:
    def __init__(self):
        self.port = None
        self.ser = None

    def scan(self):
        """
            Scan the device ports to find ESP COM port
            return -> COMx 
        """
        esp_port =None
    
        # List available serial ports
        available_ports = list(serial.tools.list_ports.comports())  

        # Iterate through Port to Find the ESP Board
        for port in available_ports:  
            port_name = port.device
            port_discription = port.description
            try:
                print(f"Try to connect to {port_name}")
            
                # Open a connection with port
                ser = serial.Serial(port_name, 9600, timeout=1)
            
                # If port discription match with the ESP discription find the board
                if "CP210x USB to UART Bridge" in port_discription: 
                    print(f"ESP Board: {port_name}")
                    esp_port = port_name
                    break
            
                # Close the connection
                ser.close() 
            
            except Exception as e:
                print(f"Failed to connect to {port_name}: {str(e)}")
            
        return esp_port
    
    def isavalable(self):
        self.port = self.scan()
        if self.port:
            return True
        return False
    
    def connect(self):
        try:
            if self.isavalable():
                self.ser = serial.Serial(self.port, 9600)
                print(f"Key Board Connected via : {self.port}")
                return True
            return False
        except Exception as e:
            print(f"Error Connecting: {str(e)}")
            return False
        
    def read(self):
        try:
            data = self.ser.read().decode('utf-8')
            if data:
                return data
            return False
        except Exception as e:
            print(f"Error Disonnecting: {str(e)}")
            return False
