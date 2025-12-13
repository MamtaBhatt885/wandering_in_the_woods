import pygame

def menu(screen):
    font = pygame.font.SysFont(None, 50)
    host_btn = font.render("HOST GAME", True, (255,255,255))
    join_btn = font.render("JOIN GAME", True, (255,255,255))

    host_rect = host_btn.get_rect(center=(400, 250))
    join_rect = join_btn.get_rect(center=(400, 350))

    while True:
        screen.fill((0, 100, 0))
        screen.blit(host_btn, host_rect)
        screen.blit(join_btn, join_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if host_rect.collidepoint(event.pos):
                    return "HOST"
                if join_rect.collidepoint(event.pos):
                    return "JOIN"

        pygame.display.update()
