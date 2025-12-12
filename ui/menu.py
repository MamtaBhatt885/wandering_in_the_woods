# ui/menu.py
import pygame
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT

def show_menu(screen):
    font = pygame.font.SysFont("arial", 32)
    title = font.render("Select Your Character", True, (255, 255, 255))

    character_paths = [
        "assets/images/person_1.png",
        "assets/images/person_2.png",
        "assets/images/person_3.png",
        "assets/images/person_4.png",
    ]

    sprites = []
    spacing = 150
    start_x = 120

    for i, path in enumerate(character_paths):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (100, 100))
        rect = img.get_rect(center=(start_x + i * spacing, 300))
        sprites.append((img, rect, path))

    while True:
        screen.fill((20, 20, 20))
        screen.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 80))

        for img, rect, _ in sprites:
            screen.blit(img, rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # quit game
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for img, rect, path in sprites:
                    if rect.collidepoint(mx, my):
                        return path  # chosen character
