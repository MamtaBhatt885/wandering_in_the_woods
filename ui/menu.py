import pygame
from ui.buttons import Button

def show_menu(window):
    start_btn = Button("Start Game", (100, 200))

    running = True
    while running:
        window.fill((34, 139, 34))  # Forest green background

        start_btn.draw(window)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.clicked(event.pos):
                    return True
