import serial.tools.list_ports

esp_port = None
SERVICE_UUID = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
CHARACTERISTIC_UUID = "beb5483e-36e1-4688-b7f5-ea07361b26a8"

def find_board():
    global esp_port  # Declare esp_port as a global variable
    
    available_ports = list(serial.tools.list_ports.comports())  # List available serial ports

    for port in available_ports:  # Search for the ESP device based on its name or other identifying information
        port_name = port.device
        port_discription = port.description
        try:
            print(f"Try to connect to {port_name}")
            ser = serial.Serial(port_name, 9600, timeout=1)
            if "CP210x USB to UART Bridge" in port_discription:
                print(f"ESP Board: {port_name}")
                esp_port = port_name
            ser.close()
        except Exception as e:
            print(f"Failed to connect to {port_name}: {str(e)}")

find_board()

