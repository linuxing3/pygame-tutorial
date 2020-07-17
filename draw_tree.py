""" 
 Show how to use a sprite backed by a graphic.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame

# The use of the main function is described in Chapter 9.

# Define some colors as global constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BROWN    = ( 100, 100, 100)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)

def draw_tree(pos1, pos2, pos3):
    pygame.draw.rect(screen, BROWN, [60, 400, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150, 400], [75, 250], [0, 400]])
    pygame.draw.polygon(screen, GREEN, [[140, 350], [75, 230], [10, 350]])

def main():
    """ Main function for the game. """
    pygame.init()
     
    pygame.display.set_caption("My Game")

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
     
     
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT



        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        draw_tree()
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(20)
        
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == "__main__":
    main()
