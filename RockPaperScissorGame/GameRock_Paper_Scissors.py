import pygame
import random
import sys

pygame.init()

# Window
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissor")

# Background gradient colors
BG_TOP = (30, 30, 60)
BG_BOTTOM = (120, 60, 160)

# UI Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 100)
RED = (255, 80, 80)
DARK_PURPLE = (40, 10, 70)
DEEP_DARK = (15, 5, 25)

# FUN FONTS (changed)
font = pygame.font.SysFont("comicsansms", 45)
small_font = pygame.font.SysFont("comicsansms", 28)
label_font = pygame.font.SysFont("comicsansms", 24)
result_font = pygame.font.SysFont("comicsansms", 32)

# Load Images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissor_img = pygame.image.load("scissor.png")

# Resize Images
rock_img = pygame.transform.scale(rock_img, (180, 180))
paper_img = pygame.transform.scale(paper_img, (180, 180))
scissor_img = pygame.transform.scale(scissor_img, (180, 180))

# Positions
rock_rect = rock_img.get_rect(topleft=(80, 350))
paper_rect = paper_img.get_rect(topleft=(360, 350))
scissor_rect = scissor_img.get_rect(topleft=(640, 350))

# Game logic
userDict = {'r': -1, 'p': 1, 's': 0}
reverseDict = {-1: 'Rock', 1: 'Paper', 0: 'Scissor'}

imageDict = {
    -1: rock_img,
     1: paper_img,
     0: scissor_img
}

result_surface = None
result_msg = ""

# Gradient
def draw_gradient():
    for y in range(HEIGHT):
        r = BG_TOP[0] + (BG_BOTTOM[0] - BG_TOP[0]) * y // HEIGHT
        g = BG_TOP[1] + (BG_BOTTOM[1] - BG_TOP[1]) * y // HEIGHT
        b = BG_TOP[2] + (BG_BOTTOM[2] - BG_TOP[2]) * y // HEIGHT
        pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

running = True

while running:

    draw_gradient()

    # Title
    title = font.render("ROCK PAPER SCISSOR", True, WHITE)
    screen.blit(title, (170, 40))

    # Choices
    screen.blit(rock_img, rock_rect)
    screen.blit(paper_img, paper_rect)
    screen.blit(scissor_img, scissor_rect)

    # Labels
    screen.blit(small_font.render("ROCK", True, WHITE), (120, 540))
    screen.blit(small_font.render("PAPER", True, WHITE), (400, 540))
    screen.blit(small_font.render("SCISSOR", True, WHITE), (670, 540))

    # Show result panel
    if result_surface:
        screen.blit(result_surface, (150, 120))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = pygame.mouse.get_pos()

            if rock_rect.collidepoint(mouse_pos):
                userinput = 'r'
            elif paper_rect.collidepoint(mouse_pos):
                userinput = 'p'
            elif scissor_rect.collidepoint(mouse_pos):
                userinput = 's'
            else:
                continue

            # Computer choice
            computer = random.choice([-1, 1, 0])
            user = userDict[userinput]

            #  WIN LOGIC FIXED
            if computer == user:
                result_msg = "DRAW"
                color = WHITE

            elif (computer == 0 and user == -1) or \
                 (computer == -1 and user == 1) or \
                 (computer == 1 and user == 0):
                result_msg = "YOU WIN!"
                color = GREEN

            else:
                result_msg = """YOU LOSE!"""
                color = RED

            # Result panel (dark purple)
            result_surface = pygame.Surface((600, 200))
            result_surface.fill(DEEP_DARK)

            pygame.draw.rect(result_surface, DARK_PURPLE, (0, 0, 600, 200), 5)

            # Images
            result_surface.blit(imageDict[user], (80, 20))
            result_surface.blit(imageDict[computer], (350, 20))

            # Labels
            you_text = label_font.render("YOU", True, GREEN)
            comp_text = label_font.render("COMPUTER", True, GREEN)

            result_surface.blit(you_text, (20, 150))
            result_surface.blit(comp_text, (450, 150))

            #  Winner text (FIXED + FUN FONT)
            win_text = result_font.render(result_msg, True, color)
            result_surface.blit(win_text, (252, 80))

    pygame.display.update()

pygame.quit()
sys.exit()
