import socket

HOST = '127.0.0.1'
PORT = 55555

class Client():
    def __init__(self):
        self.client_running = True
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(0.1)
        self.client_socket.connect((HOST, PORT))

    def receive(self, inject_signal, question_signal, scenario_signal, player_time_counter):
        while self.client_running:
            try:
                msg = self.client_socket.recv(1024).decode()
                if msg == '!DISCONNECT': print('Server disconnected'); break
                if msg.startswith('!INJECT'): inject_signal.emit(f'{msg[7:]}')
                if msg.startswith('!QUESTION'): question_signal.emit(f'{msg[9:]}')
                if msg.startswith('!SCENARIO'): scenario_signal.emit(f'{msg[9:]}')
                if msg.startswith('!TIME'): 
                    if msg[5] == '0':
                        player_time_counter.display(0)
                    else:
                        player_time_counter.display((int(msg[5:]) // 60) + 1)

            except socket.timeout:
                pass
        
        print('Closing connection')
        self.client_socket.close()

    def shutdown_client(self):
        self.client_running = False