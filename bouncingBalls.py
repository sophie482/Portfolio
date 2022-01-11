import pygame
import random

pygame.init()

width = 500
height = 400
screen = pygame.display.set_mode((width, height))
balls = []
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

class Ball:
    def __init__(self, x, y, r, colour):
        self.x = x
        self.y = y
        self.r = r
        self.colour = colour
        self.dx = random.randint(10, 20) / 10
        self.dy = random.randint(10, 20) / 10
        self.gravity = -0.05

    def drawBall(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r)
        pygame.display.flip()

    def addBall(balls, x, y):
        balls.append(Ball(x, y, 7, BLUE))

    def fall(self):
        # self.dy += self.gravity
        self.y = (self.y + self.dy)
        self.x = (self.x + self.dx)


def main():
    screen.fill(WHITE)
    done = False
    clock = pygame.time.Clock()
    while not done: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                Ball.addBall(balls, pos[0], pos[1])

        screen.fill(WHITE)
        for i in range(len(balls)):
            Ball.drawBall(balls[i])
            Ball.fall(balls[i])
    
    clock.tick(30)
    pygame.quit()

main()