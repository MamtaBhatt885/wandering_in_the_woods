# main.py

import pygame
from config.settings import *
from game.character import Character
from game.movement import random_move
from game.collision import collided
from game.stats import Stats
from ui.menu import show_menu
from ui.celebration import celebrate

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wandering in the Woods")

clock = pygame.time.Clock()

# Background
forest = pygame.image.load("woods.png")
forest = pygame.transform.scale(forest, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Music
pygame.mixer.music.load("assets/sounds/collision.wav")
pygame.mixer.music.play(-1)  # loop forever


def main_game(chosen_sprite):
    stats = Stats()

    c1 = Character(chosen_sprite, start_pos=(0, 0))
    c2 = Character("assets/images/person_2.png", start_pos=(11, 15))

    running = True

    while running:
        screen.blit(forest, (0, 0))

        # ------------------------------
        # YOUR EVENT LOOP (Works Perfectly)
        # ------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    c1.move(0, -1, GRID_ROWS, GRID_COLS)
                if event.key == pygame.K_RIGHT:
                    c1.move(0, 1, GRID_ROWS, GRID_COLS)
                if event.key == pygame.K_UP:
                    c1.move(-1, 0, GRID_ROWS, GRID_COLS)
                if event.key == pygame.K_DOWN:
                    c1.move(1, 0, GRID_ROWS, GRID_COLS)
        # ------------------------------

        # RANDOM movement for player 2
        drow2, dcol2 = random_move()
        c2.move(drow2, dcol2, GRID_ROWS, GRID_COLS)

        # Draw characters
        c1.draw(screen)
        c2.draw(screen)

        # Collision logic
        if collided(c1, c2):
            stats.finish()
            celebrate(screen)

            # ❗ Instead of RETURNING (which closes the game),
            #    wait for SPACE to restart
            font = pygame.font.SysFont("arial", 32)
            msg = font.render("Press SPACE to play again", True, (255, 255, 255))

            waiting = True
            while waiting:
                screen.blit(forest, (0, 0))
                screen.blit(msg, (WINDOW_WIDTH//2 - msg.get_width()//2, 520))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        return  # restart game

        pygame.display.update()
        clock.tick(FPS)


# Main menu → Game loop
while True:
    chosen = show_menu(screen)
    if chosen is None:
        break
    main_game(chosen)

pygame.quit()
