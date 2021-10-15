import socket 

HOST = '127.0.0.1'
PORT = 55555

class Server():
    def __init__(self):  
        self.server_running = True
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.settimeout(0.1)
        print('Server listening...')
        self.server_socket.listen()

    def send_to_all(self, message):
        for client in self.clients:
            client.sendall(message.encode())

    def accept_clients(self):
        while self.server_running:
            try:
                client, address = self.server_socket.accept()
                if client:
                    print(f'Connection from {str(address)}')
                    self.clients.append(client)
            except socket.timeout:
                pass
                
        print('Server shutting down')

    def shutdown_server(self):
        self.send_to_all('!DISCONNECT')
        self.server_running = False
        self.server_socket.close()
