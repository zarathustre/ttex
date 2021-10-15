import socket

class Client():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 55555))

    def handle_clients(self, role, message):
        self.client_socket.send(role.encode())

        if role == 'evaluator':
            self.client_socket.send(message.encode())

        elif role == 'player':
            print(self.client_socket.recv(1024).decode())

        self.client_socket.close()
