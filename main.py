import pygame
import random

# Initialize pygame
pygame.init()

width = 800
height = 600 

# Set up the display
screen = pygame.display.set_mode((width, height))

# Define the circle colors
white_circle_color = (255, 255, 252)
red_circle_color = (238, 192, 135 )

# Define the circle center and radius
circle_center = (width/2, height/2)
radius = 20

# Define the button colors
start_button_color = (124, 230, 186)
quit_button_color = (231, 151, 142)

# Define the button dimensions
start_button_width = 100
start_button_height = 50
start_button_x = screen.get_width() // 2 - start_button_width // 2
start_button_y = screen.get_height() // 2 - start_button_height // 2
start_button_rect = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)

quit_button_width = 100
quit_button_height = 50
quit_button_x = screen.get_width() // 2 - quit_button_width // 2
quit_button_y = start_button_y + start_button_height + 10
quit_button_rect = pygame.Rect(quit_button_x, quit_button_y, quit_button_width, quit_button_height)

#Generating 
font = pygame.font.Font(None, 36)
score = 0
speed = 60
alive = True

# Create a list to store the tail circles
tail = []

# Define the initial red circle position
red_circle_position = (random.randint(0, width/2), random.randint(0, height/2))

# Run the game loop

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((90, 113, 129))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
            # Check if the start button was clicked
                if start_button_rect.collidepoint(event.pos):
                    circle_center = (width/2, height/2)
                    score = 0
                    alive = True
                # Check if the quit button was clicked
                if quit_button_rect.collidepoint(event.pos):
                    running = False
    if (not alive):       
        score_text = font.render("You loose :( final score {}".format(score), True, (255, 255, 255))
        screen.blit(score_text, ((width/10)*3, (height/10)*2))
            # Draw the start button
        pygame.draw.rect(screen, start_button_color, start_button_rect)
        start_button_text = font.render("Start", True, (255, 255, 255))
        screen.blit(start_button_text, (start_button_x + 15, start_button_y + 15))

    # Draw the quit button
        pygame.draw.rect(screen, quit_button_color, quit_button_rect)
        quit_button_text = font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_button_text, (quit_button_x + 25, quit_button_y + 15))
        pygame.display.update()

    else:
        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            circle_center = (circle_center[0], circle_center[1] - 5)
        if keys[pygame.K_DOWN]:
            circle_center = (circle_center[0], circle_center[1] + 5)
        if keys[pygame.K_LEFT]:
            circle_center = (circle_center[0] - 5, circle_center[1])
        if keys[pygame.K_RIGHT]:
            circle_center = (circle_center[0] + 5, circle_center[1])

        # Check if the white circle has collided with the red circle
        if (circle_center[0] - red_circle_position[0]) ** 2 + (circle_center[1] - red_circle_position[1]) ** 2 <= radius*((radius)+radius/2) :
            score +=1
            if (speed<150):
                speed+=1
            tail.append((circle_center[0], circle_center[1]))
            red_circle_position = (random.randint(0, width-15), random.randint(0, height-15))

        #Ending when collapsing with walls
        if(circle_center[0]> width - radius  or circle_center[0] < 0 + radius or circle_center[1]> width - radius  or circle_center[1] < 0 + radius):
            alive=False

        # Update the position of the tail circles
        for i in range(len(tail) - 1, 0, -1):
            tail[i] = tail[i - 1]
        if len(tail) > 0:
            tail[0] = (circle_center[0], circle_center[1])

        # Draw the tail circles
        for tail_circle in tail:
            pygame.draw.circle(screen, white_circle_color, tail_circle, radius-2)

        # Draw the white circle
        pygame.draw.circle(screen, white_circle_color, circle_center, radius)

        # Draw the red circle
        pygame.draw.circle(screen, red_circle_color, red_circle_position, radius-(radius/3))
        score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
        screen.blit(score_text, ((width/10)*4, 10))

        # Update the display
        pygame.display.update()
        clock.tick(speed)

# Quit pygame
pygame.quit()


