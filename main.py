import pygame
import math
import random
import socket
import json
import threading
import time




# -------------------- CONFIG --------------------
WIDTH, HEIGHT = 800, 600
SERVER_PORT = 5555
SPEED = 4
# ------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wandering in the Woods")

# Assets
background = pygame.image.load("woods.png")
icon = pygame.image.load("001-walk.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("adventurer.png")
friendImg = pygame.image.load("adventurefriend.png")

font = pygame.font.Font("funfont.ttf", 32)
big_font = pygame.font.Font("funfont.ttf", 48)

# -------------------- NETWORK --------------------
class Network:
    def __init__(self, host, code):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, SERVER_PORT))
        self.client.send(code.encode())

    def send(self, data):
        self.client.send(json.dumps(data).encode())
        return json.loads(self.client.recv(2048).decode())

# -------------------- SERVER --------------------
players = []

def server_thread():
    global players
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", SERVER_PORT))
    server.listen()

    while True:
        conn, _ = server.accept()
        players.append({"x": 100, "y": 100})

        def handle(c, idx):
            while True:
                try:
                    data = json.loads(c.recv(1024).decode())
                    players[idx] = data
                    c.send(json.dumps(players).encode())
                except:
                    break

        threading.Thread(target=handle, args=(conn, len(players)-1)).start()

# -------------------- MENU --------------------
def menu():
    while True:
        screen.fill((0, 100, 0))
        host = big_font.render("HOST GAME", True, (255,255,255))
        join = big_font.render("JOIN GAME", True, (255,255,255))

        screen.blit(host, (280, 220))
        screen.blit(join, (300, 300))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if 280 < e.pos[0] < 520 and 220 < e.pos[1] < 260:
                    return "HOST"
                if 300 < e.pos[0] < 500 and 300 < e.pos[1] < 340:
                    return "JOIN"

        pygame.display.update()

# -------------------- INPUT --------------------
def get_input():
    dx = dy = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: dy -= SPEED
    if keys[pygame.K_s]: dy += SPEED
    if keys[pygame.K_a]: dx -= SPEED
    if keys[pygame.K_d]: dx += SPEED
    return dx, dy

# -------------------- COLLISION --------------------
def isCollision(x1,y1,x2,y2):
    return math.hypot(x1-x2, y1-y2) < 40

# -------------------- START --------------------
# -------------------- START --------------------
choice = menu()

if choice == "HOST":
    threading.Thread(target=server_thread, daemon=True).start()
    time.sleep(2)  # ✅ ADD IT HERE
    room_code = "WOODS"
    host_ip = "127.0.0.1"
    print("HOSTING ROOM:", room_code)

else:
    room_code = input("Enter Room Code: ")
    host_ip = input("Enter Host IP: ")


net = Network(host_ip, room_code)

player = {"x": random.randint(50,700), "y": random.randint(50,500)}

# -------------------- GAME LOOP --------------------
clock = pygame.time.Clock()
running = True
found = False

while running:
    clock.tick(60)
    screen.blit(background, (0,0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    dx, dy = get_input()
    player["x"] += dx
    player["y"] += dy

    state = net.send(player)

    for p in state:
        screen.blit(friendImg, (p["x"], p["y"]))
        if isCollision(player["x"], player["y"], p["x"], p["y"]):
            found = True

    screen.blit(playerImg, (player["x"], player["y"]))

    if found:
        text = big_font.render("FRIEND FOUND!", True, (200,0,0))
        screen.blit(text, (250, 260))

    pygame.display.update()

pygame.quit()
