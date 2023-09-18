import socket

host = "0.0.0.0"  # Listen on all available network interfaces
port = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket

server_socket.bind((host, port)) # Bind the socket to the address and port

server_socket.listen(5) # Listen for incoming connections

print(f"Listening on {host}:{port}")

while True:
    try:
        client_socket, client_address = server_socket.accept() # Accept a connection from a client

        while True:
            data = client_socket.recv(1).decode('utf-8') # Receive data from the client (one character)
            
            if not data:
                break  # No more data, break the inner loop
            
            print(data)

        client_socket.close()  # Close the client socket

    except KeyboardInterrupt:
        client_socket.close()  # Close the client socket
        break
    except Exception as e:
        print(f"An error occurred: {str(e)}")
