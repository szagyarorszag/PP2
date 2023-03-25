import pygame
import math

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PayGame Clock")
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

radius = 150
center_x, center_y = width // 2, height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill(black)
    pygame.draw.circle(screen, white, (center_x, center_y), radius, 3)
    
    for i in range(12):
        angle = i * math.pi / 6
        x = int(center_x + (radius - 20) * math.sin(angle))
        y = int(center_y - (radius - 20) * math.cos(angle))
        pygame.draw.circle(screen, white, (x, y), 5)
    
    current_time = pygame.time.get_ticks()
    seconds = (current_time // 1000) % 60
    minutes = (current_time // 60000) % 60
    
    second_angle = (seconds / 60) * 2 * math.pi
    second_x = int(center_x + (radius - 30) * math.sin(second_angle))
    second_y = int(center_y - (radius - 30) * math.cos(second_angle))
    pygame.draw.line(screen, white, (center_x, center_y), (second_x, second_y), 2)

    minute_angle = (minutes / 60) * 2 * math.pi
    minute_x = int(center_x + (radius - 50) * math.sin(minute_angle))
    minute_y = int(center_y - (radius - 50) * math.cos(minute_angle))
    pygame.draw.line(screen, white, (center_x, center_y), (minute_x, minute_y), 3)
    
    pygame.display.update()
    clock.tick(60)