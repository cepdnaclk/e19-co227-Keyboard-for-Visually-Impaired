# Author : Dasun Theekshana
# Date : 19/09/2023
# File : SerialReader.py

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
        # Get the hostname of the local machine
        hostname = socket.gethostname()

        # Get the IP address associated with the hostname
        ip = socket.gethostbyname(hostname)

        print(f"Hostname: {hostname} IP Address: {ip}")
        return ip
        
    def connect(self):
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
        try:
            self.clientsocket, self.clientip = self.server.accept()
            data = self.clientsocket.recv(1)
            if data:
                return data.decode('utf-8')
            return False
        except Exception as e:
                print(f"Error Reading: {str(e)}")
                return False