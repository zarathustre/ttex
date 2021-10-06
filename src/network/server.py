import socket 
import threading


class Server():
    def __init__(self):
        self.HEADER = 64
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER, self.PORT)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)

        self.server_running = True
        self.server.settimeout(1.0)

    
    def handle_client(self, conn, addr):
        
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode('utf-8')
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode('utf-8')
                if msg == self.DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode('utf-8'))   # send to client

        conn.close()


    def start(self):
        print("[STARTING] server is starting...")
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")

        while True:
            try:
                if not self.server_running: 
                    print('Server stopped')
                    break
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_client, args=(conn, addr))
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
            except socket.timeout as e:
                pass
