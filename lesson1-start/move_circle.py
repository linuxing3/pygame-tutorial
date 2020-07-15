# Simple pygame program

# Import and initialize the pygame library
import pygame
import random

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

ADDCIRCLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCIRCLE, 500)

circle_list = []

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ADDCIRCLE:
            startx = random.randint(100, 400)
            starty = random.randint(100, 400)
            size = random.randint(25, 75)
            color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            circle_list.append([(startx, starty), size, color ])

    # Fill the background with white
    screen.fill((255, 255, 255))

    for circle in circle_list:
        # Draw a solid blue circle in the center
        c = pygame.draw.circle(screen, circle[2], circle[0], circle[1])

        pygame.time.delay(200)
        c.move(100 * random.randint(-5 , 5), 100 * random.randint(-5, 5))

        pygame.time.delay(200)
        c.inflate(random.randint(20, 80), random.randint(20, 80))


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

