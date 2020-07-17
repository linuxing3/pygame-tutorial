"""
Show how to use an array backed grid in a graphics game.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

WIDTH  = 190
HEIGHT = 190
MARGIN = 10

# --- Create grid of numbers
# Create an empty list
grid = [[0 for x in range(4)] for y in range(4)]

# Set row 1, column 5 to zero
for x in range(4):
    for y in range(4):
        grid[x][y] = 4 * x + y + 1

class Block(pygame.sprite.Sprite):
    def __init__(self, screen, position):
        super().__init__()
        self.surf = pygame.Surface([WIDTH, HEIGHT])
        self.color = GREEN
        self.rect = pygame.draw.rect(
            screen,
            self.color,
            position
        )
        self.value = ''

    def update(self, value):
        # self.rect.flip()
        self.value = value
        self.color = RED
        pygame.transform.rotate(self.surf, 90)


block_list = [[] for x in range(4)]

pygame.init()

screen_size = [810, 810]
screen = pygame.display.set_mode(screen_size)
# Setup for sounds. Defaults are good.
pygame.display.set_caption("My Game")
pygame.mixer.init()

font = pygame.font.SysFont("arial", 64)
font_height = font.get_linesize()

# sound
collision_sound = pygame.mixer.Sound("resources/audio/qubodup-crash.ogg")
#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column_clicked = pos[0] // (WIDTH + MARGIN)
            row_clicked = pos[1] // (HEIGHT + MARGIN)
            value = str(grid[row_clicked][column_clicked])
            print("Row:", row_clicked, "Column:", column_clicked, " = ", value)
            block_clicked = block_list[row_clicked][column_clicked]
            block_clicked.update(value)
            collision_sound.play()

    # Set the screen background
    screen.fill(BLACK)

    for row in range(4):
        for column in range(4):
            if grid[row][column] == 0:
                color = WHITE
            else:
                color = GREEN
            x = MARGIN + (WIDTH + MARGIN) * column
            y = MARGIN + (HEIGHT + MARGIN) * row
            block = Block(screen, [x, y, WIDTH, HEIGHT])
            block.update(str(grid[row][column]))
            screen.blit(font.render(block.value, True, (100, 100, 100)), (x + WIDTH/4, y + HEIGHT/4))
            block_list[row].append(block)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

