import pygame
import random
import time
# import numpy

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("REAL Snake game by Boja")
pygame.init()

clock = pygame.time.Clock()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)

score = 0

def display_score(selection,font_color, font_style, font_size):
    # creating the font object
    score_font_style = pygame.font.SysFont("times new roman", 50)

    # creating the display surface object
    score_surface = score_font_style.render('Your Score : ' + str(score), True, font_color)

    # creating a rectangular object for the text placement
    score_rectangle = score_surface.get_rect()

    # displaying the text
    screen.blit(score_surface, score_rectangle)
    pygame.display.update()


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 40)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        "You lose", True, RED)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)

    # blit will draw the text on screen
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)

    pygame.quit()
    quit()



def draw_window(snake_body, food_position):
    screen.fill(PURPLE)
    for snake in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(snake[0], snake[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_position[0], food_position[1], 10, 10))
    pygame.display.update()  # in order to avoid bugs, it's best to draw both the screen and all the objects under the same function as well as having only one display update


# randomising the position of the food
food_position = [random.randrange(1, (WIDTH // 10)) * 10,
                  random.randrange(1, (HEIGHT // 10)) * 10]

snake_head = [300, 400]
snake_body = [[300, 400], [285, 400], [270, 400], [265, 400]]
direction = "RIGHT"
change_to = direction
food_spawn = True
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # moving the keys loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_p:
                print(food_position)
                print(snake_head)
                print(snake_body)

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_head[1] -= 10
    if direction == "DOWN":
        snake_head[1] += 10
    if direction == "LEFT":
        snake_head[0] -= 10
    if direction == "RIGHT":
        snake_head[0] += 10

    snake_body.insert(0, list(snake_head))
    if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = pygame.Rect((random.randrange(1, (WIDTH // 10)) * 10),
                                    (random.randrange(1, (HEIGHT // 10)) * 10), 10, 10)
        if any(food_position.collidepoint(pos) for pos in snake_body):
            food_position = pygame.Rect((random.randrange(1, (WIDTH // 10)) * 10),
                                        (random.randrange(1, (HEIGHT // 10)) * 10), 10, 10)



    food_spawn = True


    if snake_head[0] < 0 or snake_head[0] > WIDTH - 10:
        game_over()
    if snake_head[1] < 0 or snake_head[1] > HEIGHT - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            game_over()



    # in order to keep the movement orthogonal( not diagonal) i need to add elif because otherwise all the statements will be executed simultaneously
    clock.tick(25)
    draw_window(snake_body, food_position)
    display_score(1, TEAL, 'times new roman', 20)


