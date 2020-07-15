# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# [[(1, 1), (30, 30)], []]
lines = []
direction = 1
# Create a custom event for adding a new line
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            direction = random.randint(-2, 2)


    # Fill the background with white
    screen.fill((255, 255, 255))

    startx = random.randint(100, 400)
    starty = random.randint(100, 400)

    endx =  startx + direction * 100
    endy = starty + direction * 100

    lines.append([])
    
    for line in lines:
        pygame.draw.line(screen, (0, 0, 255), (startx, starty), (endx, endy), 2)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

