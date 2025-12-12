# ui/celebration.py
import pygame

def celebrate(screen):
    firework = pygame.image.load("assets/images/celebration.png").convert_alpha()
    firework = pygame.transform.scale(firework, (300, 300))

    sound = pygame.mixer.Sound("assets/sounds/collision.mp3")
    sound.play()

    for alpha in range(0, 255, 5):
        screen.fill((0, 0, 40))
        fire = firework.copy()
        fire.set_alpha(alpha)
        screen.blit(fire, (250, 150))
        pygame.display.flip()
        pygame.time.delay(30)

    pygame.time.delay(800)
