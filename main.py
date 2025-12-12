import pygame
from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game.character import Character
from game.movement import move_all
from game.collision import collided, reset_positions
from game.stats import Stats
from ui.menu import show_menu
from ui.celebration import celebrate
import pygame




pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wandering in the Woods")
clock = pygame.time.Clock()

def main_game():
    # Load background
    bg = pygame.transform.scale(
        pygame.image.load("assets/images/forest.png"),
        (WINDOW_WIDTH, WINDOW_HEIGHT)
    )

    # Two characters
    c1 = Character("assets/images/player1.png", (0, 0))
    c2 = Character("assets/images/player2.png", (9, 11))

    stats = Stats()
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_all([c1, c2])

        window.blit(bg, (0, 0))
        c1.draw(window)
        c2.draw(window)

        if collided(c1, c2):
            stats.record_meeting()
            celebrate(window)
            reset_positions(c1, c2)

        pygame.display.update()

def run():
    if show_menu(window):
        main_game()

run()
pygame.quit()

pygame.init()
pygame.mixer.init()

# Load sounds
collision_sound = pygame.mixer.Sound("sounds/collision.mp3")
bg_music = "sounds/bg_music.mp3"

# Play background music (loop forever)
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play(-1)      # -1 = infinite loop

