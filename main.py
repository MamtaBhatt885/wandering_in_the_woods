import pygame

pygame.init()
pygame.mixer.init()

# Load sounds
collision_sound = pygame.mixer.Sound("sounds/collision.mp3")
bg_music = "sounds/bg_music.mp3"

# Play background music (loop forever)
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play(-1)      # -1 = infinite loop
