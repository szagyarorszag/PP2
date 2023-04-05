import pygame
import sys
import random

# Game settings
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock() 


class Snake:
    def __init__(self):
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (0, -CELL_SIZE)

    def move(self):
        new_head_pos = (self.positions[0][0] + self.direction[0], self.positions[0][1] + self.direction[1])
        self.positions.insert(0, new_head_pos)
        self.positions.pop()

    def change_direction(self, new_direction):
        self.direction = new_direction

    def grow(self):
        self.positions.append(self.positions[-1])

    def check_collision(self):
        if self.positions[0] in self.positions[1:]:
            return True
        if self.positions[0][0] < 0 or self.positions[0][1] < 0 or self.positions[0][0] >= WIDTH or self.positions[0][1] >= HEIGHT:
            return True
        return False

    def draw(self, screen):
        for position in self.positions:
            pygame.draw.rect(screen, GREEN, pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self, snake):
        self.position = self.generate_random_position(snake)

    def generate_random_position(self, snake):
        while True:
            position = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                        random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
            if position not in snake.positions:
                return position

    def draw(self, screen):
        pygame.draw.rect(screen, RED, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))
    def main():
        snake = Snake()
        food = Food(snake)
        score = 0
        level = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.change_direction((0, -CELL_SIZE))
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                    snake.change_direction((0, CELL_SIZE))
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.change_direction((-CELL_SIZE, 0))
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.change_direction((CELL_SIZE, 0))

        snake.move()

        if snake.positions[0] == food.position:
            snake.grow()
            food = Food(snake)
            score += 1

            if score % 3 == 0:
                level += 1
                FPS += 2

        if snake.check_collision():
            break

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)

        # Display score and level
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score} Level: {level}", True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

main()