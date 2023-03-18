import socket
import sys


def setup_client(host, port):
    client = None

    ################## ADD YOUR CODE HERE	##################
    client_socket = socket.socket()  # instantiate
    # ##print(host)
    client_socket.connect((host, port))  # connect to the server
    client = client_socket
    ##########################################################
    return client


def receive_message_via_socket(client):
    message = None
    global remaining_data
    ################## ADD YOUR CODE HERE	##################
    if remaining_data:
        data = client.recv(1024)
        message = data.decode()
        remaining_data = remaining_data[len(data):]
        return message
    else:
        data = client.recv(1024)
        message_length = int(data[:10])
        message = data[10:message_length + 10].decode()
        remaining_data = data[message_length + 10:]
        return message

    # print("message received "+ message)
    ##########################################################


def send_message_via_socket(client, message):
    ################## ADD YOUR CODE HERE	##################
    # @time.sleep(0.1)
    # print("message send "+message)
    message_length = str(len(message)).ljust(10)
    client.send(message_length.encode() + message.encode())


host = '192.168.137.41'
port = 5050
try:
    client = setup_client(host, port)

except socket.error as error:
    # print("Error in setting up server")
    print(error)
    sys.exit()
message = receive_message_via_socket(client)
print(message)
