import pygame
import sys  # This isn't in main yet?

#stuff we probably already have:
pygame.init()
font = pygame.font.Font('funfont.ttf', 36)



menu_state = "main"  # tracks which menu is active
grade_selected = None
forest_selected = None
players = None
width = None
depth = None



class Button:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action

    def draw(self):
        # what the button looks like
        mouse_pos = pygame.mouse.get_pos()
        color = DARK_BLUE if self.rect.collidepoint(mouse_pos) else BLUE
        pygame.draw.rect(screen, color, self.rect)
        # what the text looks like
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.action()





def start_new_game():
    global menu_state
    menu_state = "choose_grade"

def select_grade(grade):
    global menu_state, grade_selected
    grade_selected = grade
    if grade == "K-2":
        menu_state = "choose_forest"
    else:
        menu_state = "choose_players"

def select_forest(size):
    global forest_selected
    forest_selected = size
    print(f"Grade {grade_selected}, Forest: {forest_selected} selected")
    # proceed to game start if needed

def select_players(num):
    global players
    players = num
    print(f"{players} Players selected")

def select_width(val):
    global width
    width = val
    print(f"Width set to {width} miles")

def select_depth(val):
    global depth
    depth = val
    print(f"Depth set to {depth} miles")

# --- Generate buttons dynamically ---
def get_buttons():
    buttons = []

    # Always show "Start a New Game"
    buttons.append(Button(50, 50, 200, 50, "Start a New Game", start_new_game))

    if menu_state == "choose_grade":
        # Select grade level
        buttons.append(Button(50, 120, 200, 50, "Grades K-2", lambda: select_grade("K-2")))
        buttons.append(Button(50, 180, 200, 50, "Grades 3-5", lambda: select_grade("3-5")))
        buttons.append(Button(50, 240, 200, 50, "Grades 6-8", lambda: select_grade("6-8")))

    elif menu_state == "choose_forest":
        # Size of square "forrest" grid
        buttons.append(Button(50, 120, 250, 50, "16 Square Mile Forest", lambda: select_forest(16)))
        buttons.append(Button(50, 180, 250, 50, "25 Square Mile Forest", lambda: select_forest(25)))
        buttons.append(Button(50, 240, 250, 50, "36 Square Mile Forest", lambda: select_forest(36)))

    elif menu_state == "choose_players":
        # Number of players buttons
        buttons.append(Button(50, 120, 150, 50, "2 Players", lambda: select_players(2)))
        buttons.append(Button(220, 120, 150, 50, "3 Players", lambda: select_players(3)))
        buttons.append(Button(390, 120, 150, 50, "4 Players", lambda: select_players(4)))

        # Width of the "forrest" grid buttons
        buttons.append(Button(50, 200, 150, 50, "4 Miles Wide", lambda: select_width(4)))
        buttons.append(Button(220, 200, 150, 50, "5 Miles Wide", lambda: select_width(5)))
        buttons.append(Button(390, 200, 150, 50, "6 Miles Wide", lambda: select_width(6)))

        # Depth of the "forrest" grid buttons
        buttons.append(Button(50, 280, 150, 50, "4 Miles Deep", lambda: select_depth(4)))
        buttons.append(Button(220, 280, 150, 50, "5 Miles Deep", lambda: select_depth(5)))
        buttons.append(Button(390, 280, 150, 50, "6 Miles Deep", lambda: select_depth(6)))

    return buttons

# Incorporate into main
while True:
    buttons = get_buttons()

    # check how we might need this, maybe not?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.click()

    # Draw all buttons
    for button in buttons:
        button.draw()

    pygame.display.flip()
    # not totally sure how to incorporate this all, but maybe this is a good start?
    # also, maybe I should change "Start" button to "Menu" (Menu will always be displayed?), then
    # after the user makes their selections pressing "Start" will start the game timer.
