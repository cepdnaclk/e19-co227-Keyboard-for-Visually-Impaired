import socket

# Define the IP address and port to listen on (use the same IP as ESP32)
HOST = '192.168.4.1'  # Replace with your ESP32's IP address
PORT = 80

# Create a socket and bind it to the specified IP and port
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

try:
    while True:
        # Accept incoming connection
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Read data from the ESP32
        data = client_socket.recv(1024).decode("utf-8")
        if data:
            print(f"Received data: {data}")

        # Close the client socket
        client_socket.close()

except KeyboardInterrupt:
    print("Server stopped.")
finally:
    # Close the server socket
    server_socket.close()
