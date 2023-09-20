# Author : Dasun Theekshana
# Date : 19/09/2023
# File : SerialReader.py

import serial
import serial.tools.list_ports

class ESPSerialReader:
    def __init__(self):
        self.port = None    # Stores the name of the ESP COM port (e.g., COMx)
        self.ser = None     # Stores the serial connection object

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
            
                # Open a connection with the port at 9600 baud rate with a timeout of 1 second
                ser = serial.Serial(port_name, 9600, timeout=1)
            
                # If the port description matches the ESP board's description, identify it
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
        """
        Check if an ESP board is available by calling the scan method.

        Returns:
            bool: True if an ESP board is available, False otherwise.
        """
        self.port = self.scan()
        if self.port:
            return True
        return False
    
    def connect(self):
        """
        Connect to an available ESP board via serial communication.

        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        try:
            if self.isavalable():
                 # If an ESP board is available, establish a serial connection to it
                self.ser = serial.Serial(self.port, 9600)
                print(f"Key Board Connected via : {self.port}")
                self.ser.write(0)
                return True
            return False
        except Exception as e:
            print(f"Error Connecting: {str(e)}")
            return False
        
    def read(self):
        """
        Read data from the connected ESP board via serial communication.

        Returns:
            str or False: The read data as a string if available, or False if an error occurs.
        """
        try:
            data = self.ser.read().decode('utf-8')  # Read data from the serial connection
            if data:
                return data
            return False
        except Exception as e:
            print(f"Error Disonnecting: {str(e)}")
            return False
