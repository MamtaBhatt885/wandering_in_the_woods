import pygame
import math
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600)) # (width, height)

# Background
background = pygame.image.load('woods.png')

# Title and Icon
pygame.display.set_caption("Wandering in the Woods")
icon = pygame.image.load('001-walk.png') # Use flatiron.com to download a 32x png
pygame.display.set_icon(icon)

# Player (must
playerImg = pygame.image.load('adventurer.png') # flatiron.com 64xpng
playerX = 370 # X coordinate of player = towards middle
playerY = 480 # Y coordinate of player = towards bottom
playerX_change = 0 # provides option to move player left and right

# Friend
friendImg = pygame.image.load('adventurefriend.png') # 64xpng by max.icons - Flaticon</a> <a href="https://www.flaticon.com/free-icons/hiker" title="hiker icons">Hiker
friendX = random.randint(0, 736) # (smallest, largest) poss random int
friendY = random.randint(50, 105)
friendX_change = 1
friendY_change = 40

# Score
score_value = 0
font = pygame.font.Font('funfont.ttf', 32) # font type, font size ...find more fonts at dafont.com "Super Croissant"

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('funfont.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (50, 150, 100)) # RGB= Blue (out of 255)
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("Friend Found!", True, (150, 0, 0)) # Red
    screen.blit(over_text, (300, 250)) #middle of screen

def player(x,y):
    screen.blit(playerImg, (x, y))

def friend(x,y):
    screen.blit(friendImg, (x, y))

def isCollision(playerX, playerY, friendX, friendY):
    distance = math.sqrt((math.pow(playerX-friendX, 2)) + (math.pow(playerY-friendY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:

    # RGB + Red, Green, Blue
    screen.fill((0, 100, 0))  # green
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystroke pressed, check right or left
    if event.type == pygame.KEYDOWN: # "DOWN" means a key is pressed
        if event.key == pygame.K_LEFT: # Left arrow key
            print("Left arrow pressed")
            playerX_change = -1
        if event.key == pygame.K_RIGHT: # Right arrow key
            print("Right arrow pressed")
            playerX_change = 1
    if event.type == pygame.KEYUP: # "UP" means a key has been released
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("Keystroke has been released")
            playerX_change = 0

    # Keep player within the boundaries of the screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Move friend back and forth within boundary of screen
    friendX += friendX_change

    if friendX <= 0:
        friendX_change = 1
        friendY += friendY_change
    elif friendX >= 736:
        friendX_change = -1
        friendY += friendY_change

    # Game Over
    if friendY > 200 and friendX == playerX:
        game_over_text()
        break


    # Collision
    collision = isCollision(friendX, friendY, playerX, playerY)
    if collision:
        print("You have found your friend")

    player(playerX, playerY)
    friend(friendX, friendY)
    show_score(textX, textY)
    pygame.display.update() # Display should always be updating

