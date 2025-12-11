### Does this need to be in main?:
# from ui.celebration import celebration_scene

### Maybe add to the collision folder?:
# if characters_collide(player1, player2):
#     elapsed = timer.get_elapsed()
#     celebration_scene(screen, elapsed, reset_game)
###


### If we haven't already imported:
import pygame
import time
import random
import threading
import pyttsx3   # I think this works for text-to-speech
############## have you used pyttsx3 before?


# Audible announcememt
def speak_elapsed_time(seconds):
    def _speak():
        engine = pyttsx3.init()
        engine.say(f"Congratulations! You found your friend in {seconds:.2f} seconds.")
        engine.runAndWait()
    threading.Thread(target=_speak).start()


# Make confetti
class ConfettiParticle:
    def __init__(self, screen_width, screen_height):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-50, -10)
        self.speed = random.uniform(2, 5)
        self.color = random.choice([
            (255, 0, 0), (0, 255, 0), (0, 128, 255),
            (255, 255, 0), (255, 0, 255), (255, 128, 0)
        ])
        self.size = random.randint(4, 10)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


# Celebration scene -- Confetti, read and show congrats & elapsed time, reset
def celebration_scene(screen, elapsed_time, reset_callback):

    # confetti
    confetti_list = [ConfettiParticle(width, height) for _ in range(150)]

    # announce elapsed time (using TTS)
    speak_elapsed_time(elapsed_time)

    # length of time of celebration
    celebration_start = time.time()

    running = True
    while running:
        current = time.time()
        if current - celebration_start > 7:   # celebration lasts 7
            reset_callback()
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # display congrats
        title_surface = LARGE_FONT.render("You found your friend!", True, BLACK)
        screen.blit(title_surface, (width//2 - title_surface.get_width()//2, 80))

        # display elapsed time
        t_surface = MEDIUM_FONT.render(f"It took you {elapsed_time:.2f} seconds.", True, BLACK)
        screen.blit(t_surface, (width//2 - t_surface.get_width()//2, 180))

        # throw confetti
        for c in confetti_list:
            c.update()
            c.draw(screen)
            if c.y > height:
                c.__init__(width, height)   # reset confetti pieces

        pygame.display.flip()
        pygame.time.delay(16)  # ~60 FPS
