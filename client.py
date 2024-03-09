import socket
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 7777))

# Receive and print the welcome message from the server
welcome_message = client_socket.recv(1024).decode("utf-8")
print(welcome_message)

try:
    while True:
        # Send a message to the server
        message = input("Your message: ")
        client_socket.send(message.encode("utf-8"))

        # Receive and print the server's reply
        data = client_socket.recv(1024).decode("utf-8")
        print(f"Received data: {data}")

        # Check if the server wants to end the conversation
        if data.lower() == "bye":
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection after the conversation
    client_socket.close()
