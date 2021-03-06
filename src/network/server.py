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
        self.nicknames = [1,2,3,4,5,6,7,8,9]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.settimeout(0.1)
        self.server_signal = ServerSignals()
        print('Server listening...')
        self.server_socket.listen()

    def shutdown_server(self):
        if len(self.clients) != 0:
            self.send_to_all('!DISCONNECT')
        self.server_running = False

    @Slot(str)
    def send_time(self, time):
        self.send_to_all(f'!TIME{time}')

    def send_to_all(self, message):
        for client in self.clients:
            client.sendall(message.encode())

    def assign_nickname(self):
        self.nicknames.sort()
        first_nick = self.nicknames[0]
        self.nicknames.remove(first_nick)
        return str(first_nick)

    def accept_clients(self, msg):
        while self.server_running:
            try:
                client, address = self.server_socket.accept()
                if client:
                    nick = self.assign_nickname()
                    client.sendall(f'{msg}{nick}'.encode())                # scenario text
                    print(f'Connection from {address}')
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
                if msg.startswith('!DISC'):
                    self.clients.remove(client)
                    self.server_signal.server_signal.emit(len(self.clients))
                    self.nicknames.append(int(msg[-1]))
                
                if msg.startswith('!ANSWER'):
                    self.server_signal.receive_answer_signal.emit(f'{msg[7:]}')
            except socket.timeout:
                pass
