from PySide6.QtCore import QObject, Signal, Slot

import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

class ServerSignals(QObject):
    server_signal = Signal(int)
    receive_answer_signal = Signal(str)

class Server():
    def __init__(self):  
        self.server_running = True
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.settimeout(0.1)
        self.server_signal = ServerSignals()
        print('Server listening...')
        self.server_socket.listen()

    @Slot(str)
    def send_time(self, time):
        self.send_to_all(f'!TIME{time}')

    def send_to_all(self, message):
        for client in self.clients:
            client.sendall(message.encode())

    def accept_clients(self, msg):
        while self.server_running:
            try:
                client, address = self.server_socket.accept()
                if client:
                    client.sendall(msg.encode())                # scenario text
                    print(f'Connection from {str(address)}')
                    self.clients.append(client)
                    self.server_signal.server_signal.emit(len(self.clients))

                    receive_dc_thread = threading.Thread(target=self.receive_message, args=(client, ), daemon=True)
                    receive_dc_thread.start()
               
            except socket.timeout:
                pass
                
        print('Server shutting down')
        self.server_socket.close()

    def receive_message(self, client):
        while self.server_running:
            try:
                msg = client.recv(1024).decode()
                if msg == '!DISC':
                    self.clients.remove(client)
                    self.server_signal.server_signal.emit(len(self.clients))
                
                if msg.startswith('!ANSWER'):
                    self.server_signal.receive_answer_signal.emit(f'{msg[7:]}')
            except socket.timeout:
                pass

    def shutdown_server(self):
        if len(self.clients) != 0:
            self.send_to_all('!DISCONNECT')
        self.server_running = False
