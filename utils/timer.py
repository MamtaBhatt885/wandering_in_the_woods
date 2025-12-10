# TIMER

game_started = False
timer_running = False
start_ticks = 0
time_elapsed = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # time starts when player hits the start button
            if start_button.collidepoint(event.pos):
                game_started = True
                timer_running = True
                start_ticks = pygame.time.get_ticks()  # starts the timer in pygame

# Stop the timer
    if collision:
        timer_running = False
        time_elapsed = (pygame.time.get_ticks() - start_ticks) / 1000
        print(f"You found your friend! That took {time_elapsed:.2f} seconds")

