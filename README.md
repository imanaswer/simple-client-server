# simple-client-server
"Simple Python client-server communication using sockets. Exchange messages until 'bye' for a basic conversation. Suitable for learning socket programming and server-client interactions in Python."


# Simple Client-Server Communication

This is a basic client-server communication project using Python sockets. The client and server exchange messages until the client sends "bye" to end the conversation.

## Getting Started

### Prerequisites

- Python 3.x

### Running the Server

1. Open a terminal.
2. Navigate to the server directory.
3. Run the server script:

    ```bash
    python server.py
    ```

4. The server will start listening for connections on port 1111.

### Running the Client

1. Open a separate terminal.
2. Navigate to the client directory.
3. Run the client script:

    ```bash
    python client.py
    ```

4. The client will connect to the server at the IP address "127.0.0.1" and port 7777.

## Usage

1. After connecting, the server sends a welcome message to the client.
2. Enter your message when prompted by the client script.
3. The server receives the message, processes it, and sends a response back to the client.
4. The conversation continues until the client enters "bye" to end it.

## Notes

- The server and client scripts are basic examples and may need modifications for production use.
- Ensure that the server is running before attempting to connect with the client.


## Acknowledgments

- Thanks to the [cryptography](https://cryptography.io/en/latest/) library for secure communication.
- Inspired by simple client-server examples on various programming forums.

Feel free to contribute or report issues!
