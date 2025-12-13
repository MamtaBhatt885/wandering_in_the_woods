import socket, threading, random, string, json

HOST = "0.0.0.0"
PORT = 5555

rooms = {}

def generate_code():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server running...")

def handle_client(conn):
    code = conn.recv(1024).decode()

    if code not in rooms:
        rooms[code] = []

    rooms[code].append({"x": 100, "y": 100})

    while True:
        try:
            data = json.loads(conn.recv(1024).decode())
            rooms[code][0] = data
            conn.send(json.dumps(rooms[code]).encode())
        except:
            break

    conn.close()

while True:
    conn, _ = server.accept()
    threading.Thread(target=handle_client, args=(conn,)).start()
