import pygame

def handle_arrow_keys(character, rows, cols):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        character.move(-1, 0, rows, cols)  # Up arrow button moves up one row
    elif keys[pygame.K_DOWN]:
        character.move(1, 0, rows, cols)  # Down arrow button moves down one row
    elif keys[pygame.K_LEFT]:
        character.move(0, -1, rows, cols)  # Left arrow button moves left one column
    elif keys[pygame.K_RIGHT]:
        character.move(0, 1, rows, cols)  # Right arrow button moves right one column