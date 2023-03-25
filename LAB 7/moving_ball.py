import pygame
pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_color = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20
            elif event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20

    if ball_x - ball_radius >= 0:
        ball_x = max(ball_x - 20, ball_radius)
    if ball_x + ball_radius <= screen_width:
        ball_x = min(ball_x + 20, screen_width - ball_radius)
    if ball_y - ball_radius >= 0:
        ball_y = max(ball_y - 20, ball_radius)
    if ball_y + ball_radius <= screen_height:
        ball_y = min(ball_y + 20, screen_height - ball_radius)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()

    clock.tick(30)
