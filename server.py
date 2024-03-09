import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 1111))
server_socket.listen(5)

print("Waiting for connection...")

while True:
    client, client_address = server_socket.accept()
    print(f"{client_address} has connected.")

    # Send a welcome message to the client
    client.send(b"Hello, client!")

    while True:
        # Receive data from the client
        data = client.recv(1024).decode("utf-8")

        # Check if the client wants to end the conversation
        if data.lower() == "bye":
            print(f"{client_address} has disconnected.")
            break

        print(f"Received data from {client_address}: {data}")

        # Send a response back to the client
        response = f"Server received: {data}"
        client.send(response.encode("utf-8"))

    # Close the connection
    client.close()
