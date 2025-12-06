import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600)) # (width, height)

# Title and Icon
pygame.display.set_caption("Wandering in the Woods")
# Use flatiron.com to download a 32x png
icon = pygame.image.load('001-walk.png')
pygame.display.set_icon(icon)

# Player (must
playerImg = pygame.image.load('adventurer.png') # flatiron.com 64xpng
playerX = 370 # X coordinate of player = middle
playerY = 480 # Y coordinate of player = towards bottom

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:

    screen.fill((0, 128, 0))  # RGB
    playerX += 0.2 # moves the player to the right
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False



    player(playerX, playerY)
    pygame.display.update() # Display should always be updating
