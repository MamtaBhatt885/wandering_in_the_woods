import pygame
import time

def celebrate(window):
    font = pygame.font.SysFont("Arial", 40)
    label = font.render("They met! 🎉", True, (255, 255, 255))

    window.blit(label, (100, 150))
    pygame.display.update()
    time.sleep(2)
