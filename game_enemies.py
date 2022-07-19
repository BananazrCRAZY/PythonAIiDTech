import pygame, sys, random

# First thing in any pygame program - initializes pygame's internal variables.
pygame.init()

# set up variables for the screen size in pixels
size = width, height = 640, 480

# initialize a window with the screen size you set
screen = pygame.display.set_mode(size)

# create a clock, which will be used to control the program's frame rate
clock = pygame.time.Clock()

# create variables to store location and size of a shape to draw on screen.
shape_position = (width / 2, height / 2)
shape_size = (100, 100)

# make a pygame.Rect variable for the shape:
shape_rect = pygame.Rect(shape_position, shape_size)

# RGB colors of the shapes to draw
shape_color = (142, 58, 60)
line_color = (51, 116, 48)
circle_color = (143, 122, 59)

# Coin
coin_color = (255, 255, 0)
coin_pos = (600, 400)
coin_radius = 10

# Coin collision box
coin_collision = pygame.Rect(coin_pos[0] - coin_radius, coin_pos[1] - coin_radius,
                             coin_radius * 2, coin_radius * 2)
coin_collected = False

# Player position
# Refactor and update to 'player' instead of circle if time
circle_pos = (50, 50)
circle_radius = 25

# Player collision box
player_collision = pygame.Rect(circle_pos[0] - circle_radius, circle_pos[1] - circle_radius,
                               circle_radius * 2, circle_radius * 2)

# Enemies
enemy_positions = []
enemy_count = 3

enemy_rect = pygame.Rect(0, 0, 60, 60)

for _ in range(enemy_count):
    pos_x = random.randint(0, width)
    pos_y = random.randint(0, height)
    pos = pygame.Vector2(pos_x, pos_y)
    enemy_positions.append(pos)

player_alive = True

move_right = False
move_left = False
move_up = False
move_down = False

# Game loop
while not coin_collected:
    # tick forward at 60 frames per second
    clock.tick(200)

    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            sys.exit()
        # This event happens when a key is pressed.
        elif event.type == pygame.KEYDOWN:
            # This checks to see if the key that was pressed is the left arrow key.
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            # elif to continue
        # This event happens when a key is released
        elif event.type == pygame.KEYUP:
            # This checks to see if the key that was released is the left arrow key.
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_DOWN:
                move_down = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            # elif to continue

    # This could be made into a function to clean up if there's time.
    if move_right:
        circle_pos = (circle_pos[0] + 10 // 10, circle_pos[1])
    elif move_left:
        circle_pos = (circle_pos[0] - 10 // 10, circle_pos[1])
    elif move_down:
        circle_pos = (circle_pos[0], circle_pos[1] + 10 // 10)
    elif move_up:
        circle_pos = (circle_pos[0], circle_pos[1] - 10 // 10)

    # Update the player's collision box position.
    player_collision = pygame.Rect(circle_pos[0] - circle_radius, circle_pos[1] - circle_radius,
                                   circle_radius * 2, circle_radius * 2)

    # Extension Question: should you use if or elif statements for the other movement options?
    # Fill the screen with a solid color.
    # Comment this out to "paint" a picture with player movement.
    screen.fill((50, 50, 100))

    # Fill a rectangular area with the shape color. This is the fastest way to draw rectangles to the screen.
    # screen.fill(shape_color, rect=shape_rect)

    if player_collision.colliderect(coin_collision):
        print("You're colliding with the coin")
        coin_collected = True
        # make the coin invisible
        # move the coin off screen
        # indicate the player got a coin

    for position in enemy_positions:
        # move the rect
        player_position = pygame.Vector2(circle_pos)
        direction_vector = player_position - position  # vector from enemy to player
        direction_vector.normalize_ip()
        direction_vector *= .2
        position += direction_vector

        enemy_rect.center = position

        if player_collision.colliderect(enemy_rect):
            player_alive = False

        screen.fill(shape_color, rect=enemy_rect)

    # Draws a circle on the given surface, color, position, and radius.
    # This is the 'player' for our purposes
    if player_alive:
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
    # Draw the player's collision box
    # screen.fill(circle_color, rect = player_collision)

    if not coin_collected:
        # Draw a coin
        pygame.draw.circle(screen, coin_color, coin_pos, coin_radius)
        # Draw the coin's collision box for testing
        # screen.fill(coin_color, rect=coin_collision)

    # Draws a line on the given surface, color, start position, end position, and line width in pixels.
    # This draws a line between the two shapes
    # pygame.draw.line(screen, line_color, circle_pos, shape_rect.center, 4)

    # At the end of each game loop, call pygame.display.flip() to update the screen with what you drew.
    pygame.display.flip()