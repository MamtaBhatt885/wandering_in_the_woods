def get_input():
    dx = dy = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: dy = -2
    if keys[pygame.K_s]: dy = 2
    if keys[pygame.K_a]: dx = -2
    if keys[pygame.K_d]: dx = 2
    return dx, dy
