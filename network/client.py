import socket, json

class Network:
    def __init__(self, code):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("SERVER_IP_HERE", 5555))
        self.client.send(code.encode())

    def send(self, data):
        self.client.send(json.dumps(data).encode())
        return json.loads(self.client.recv(2048).decode())
