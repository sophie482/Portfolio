import arcade
import random

width = 600
height = 600
balls = []

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.size = 0
        self.colour = None

    def makeBall():
        ball = Ball()
        ball.size = random.randint(10, 20)

        ball.x = random.randint(ball.size, width - ball.size)
        ball.y = random.randint(ball.size, height - ball.size)

        ball.dx = random.randint(-2, 3)
        ball.dy = random.randint(-2, 3)

        ball.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        return ball

    def draw(self):
        for ball in balls: 
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.colour)

    def moveBall(self):
        for ball in balls:
            ball.x += ball.dx
            ball.y += ball.dy

            if ball.x < ball.size:
                ball.dx *= -1
            if ball.y < ball.size:
                ball.dy *= -1
            if ball.x > width - ball.size:
                ball.dx *= -1
            if ball.y > height - ball.size:
                ball.dy *= - 1

def main():
    # width, height, title, resizable, antialiasing
    arcade.open_window(width, height, "Bouncing Balls", False, True)
    # start drawing (similar to pygame.init())
    arcade.start_render()

    # create/draw/move balls
    for i in range(0, 6):

        ball = Ball.makeBall()
        balls.append(ball)
        Ball.draw(ball)
    
    while True: 
        Ball.moveBall(ball)

    # stop drawing (without this the drawing flashes)
    arcade.finish_render()

    arcade.run()


main()


    # def on_mouse_press(self):
    #     ball = Ball.makeBall()
    #     self.balls.append(ball)


