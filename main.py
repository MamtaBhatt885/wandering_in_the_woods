import pygame
from config import *
from grid import Grid
from player import Player
from simulation import Simulation
from stats import Stats

# ================= INIT =================
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Wandering in the Woods")
clock = pygame.time.Clock()

# ================= ASSETS =================
background = pygame.image.load("assets/background.png").convert_alpha()

background = pygame.transform.smoothscale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

sprite = pygame.image.load("assets/sprite.png").convert_alpha()
sprite = pygame.transform.scale(sprite, (CELL_SIZE, CELL_SIZE))

meet_sound = pygame.mixer.Sound("assets/meet.wav")

font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 40)

# ================= STATE =================
phase = "INPUT"   # INPUT → PLACE → GAME
rows, cols = 6, 6
num_players = 2

placed_players = []
grid = None
simulation = None
run_moves = 0

stats = Stats()
running = True

# ================= HELPERS =================
def cell_from_mouse(pos):
    x, y = pos
    col = (x - grid.offset_x) // CELL_SIZE
    row = (y - grid.offset_y) // CELL_SIZE
    return row, col

def cell_occupied(r, c):
    return any(p.row == r and p.col == c for p in placed_players)

# ================= LOOP =================
screen.blit(background, (0, 0))


while running:
    clock.tick(FPS)



    # ---------- DRAW FOREST ONLY AT BOTTOM ----------
    FOREST_HEIGHT = SCREEN_HEIGHT // 3  # bottom 1/3 of screen

    screen.blit(
        background,(0,0)    )


    # ================= EVENTS =================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---------- INPUT PHASE ----------
        if phase == "INPUT" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rows = min(rows + 1, 12)
            if event.key == pygame.K_DOWN:
                rows = max(rows - 1, 4)
            if event.key == pygame.K_RIGHT:
                cols = min(cols + 1, 12)
            if event.key == pygame.K_LEFT:
                cols = max(cols - 1, 4)

            if event.key in (pygame.K_2, pygame.K_3, pygame.K_4):
                num_players = int(event.unicode)

            if event.key == pygame.K_RETURN:
                placed_players = []
                grid = Grid(rows, cols)
                phase = "PLACE"

        # ---------- PLACEMENT PHASE ----------
        elif phase == "PLACE":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if len(placed_players) < num_players:
                    r, c = cell_from_mouse(event.pos)
                    if 0 <= r < rows and 0 <= c < cols and not cell_occupied(r, c):
                        placed_players.append(Player(len(placed_players) + 1, r, c))

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if len(placed_players) == num_players:
                    simulation = Simulation(rows, cols, placed_players, meet_sound)
                    run_moves = 0
                    phase = "GAME"

        # ---------- REPLAY ----------
        elif phase == "GAME" and event.type == pygame.KEYDOWN and simulation.finished:
            stats.add_run(run_moves)
            phase = "INPUT"

    # ================= DRAW =================
    if phase == "INPUT":
        title = big_font.render("SETUP ", True, (0, 0, 0))
        screen.blit(title, (280, 80))

        lines = [
            f"Rows (↑ ↓): {rows}",
            f"Columns (← →): {cols}",
            f"Players (2 / 3 / 4): {num_players}",
            "Press ENTER to continue",
        ]

        for i, line in enumerate(lines):
            screen.blit(
                font.render(line, True, (0, 0, 0)),
                (300, 180 + i * 40),
            )

    elif phase == "PLACE":
        grid.draw(screen)

        for p in placed_players:
            screen.blit(
                sprite,
                (
                    grid.offset_x + p.col * CELL_SIZE,
                    grid.offset_y + p.row * CELL_SIZE,
                ),
            )

        info = font.render(
            f"Click to place players ({len(placed_players)}/{num_players})",
            True,
            (0, 0, 0),
        )
        screen.blit(info, (20, SCREEN_HEIGHT - 40))

    else:  # GAME
        grid.draw(screen)

        if not simulation.finished:
            simulation.step()
            run_moves += 1

        for p in simulation.players:
            screen.blit(
                sprite,
                (
                    grid.offset_x + p.col * CELL_SIZE,
                    grid.offset_y + p.row * CELL_SIZE,
                ),
            )

        min_r, max_r, avg_r = stats.summary()
        stats_text = f"Runs: {len(stats.runs)} | Min: {min_r}  Max: {max_r}  Avg: {avg_r:.1f}"
        screen.blit(
            font.render(stats_text, True, (0, 0, 0)),
            (10, SCREEN_HEIGHT - 40),
        )

        if simulation.finished:
            done = font.render("MEET! Press any key to restart", True, (0, 0, 0))
            screen.blit(done, (260, SCREEN_HEIGHT - 80))

    pygame.display.flip()

pygame.quit()
