# Author : Dasun Theekshana
# Date : 19/09/2023
# File : WiFiReader.py

import socket

#host = "0.0.0.0"  
port = 8888

class ESPWifiReader:
    def __init__(self, host):
        # Listen on all available network interfaces
        self.server = None
        self.clientsocket = None
        self.clientip = None
        self.host = host
        
    def scan(self):
        """
        Scan and retrieve the IP address of the local machine.

        Returns:
            str: The IP address of the local machine.
        """
        # Get the hostname of the local machine
        hostname = socket.gethostname()

        # Get the IP address associated with the hostname
        ip = socket.gethostbyname(hostname)

        print(f"Hostname: {hostname} IP Address: {ip}")
        return ip
        
    def connect(self):
        """
        Establish a socket server and listen for incoming connections.

        Returns:
            bool: True if the server is successfully started, False otherwise.
        """
        try:
            ip = self.scan()
            
            # Create a socket
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

            # Bind the socket to the address and port
            self.server.bind((self.host, port)) 

            # Listen for incoming connections
            self.server.listen(5)
            
            print(f"Connected with: {ip} ({port})")
            return True
            
        except Exception as e:
            print(f"Error Connecting: {str(e)}")
            return False
        
    def disconnect(self):
        """
        Disconnect the client socket and close the server socket.

        Returns:
            bool: True if disconnection is successful, False otherwise.
        """
        try:
            if self.server:
                self.clientsocket.close()
                self.server.close()
                return True
            return False
        except Exception as e:
                print(f"Error Disonnecting: {str(e)}")
                return False
        
    def read(self):
        """
        Read data from the connected client socket.

        Returns:
            str or False: The read data as a string if available, or False if an error occurs.
        """
        try:
            self.clientsocket, self.clientip = self.server.accept()
            data = self.clientsocket.recv(2)
            if data:
                return data.decode('utf-8')
            return False
        except Exception as e:
                print(f"Error Reading: {str(e)}")
                return False

# Example usage:
# reader = ESPWifiReader("0.0.0.0")
# if reader.connect():
#     data = reader.read()
#     # Process the received data
#     print(f"Received data: {data}")
#     reader.disconnect()