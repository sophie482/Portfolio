
import arcade
import random

width = 600
height = 600

class Ball:
    def __init__(self):
        self.colour = None
        self.size = 0
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    def createBall(x, y):
        ball = Ball()

        ball.colour = ((random.randint(0, 255)), (random.randint(0, 255)), random.randint(0, 255))

        ball.size = random.randint(10, 20)

        ball.x = x
        ball.y = y

        ball.dx = random.randint(-5, 6)
        ball.dy = random.randint(-5, 6)

        return ball

class ballGame(arcade.Window):

    def __init__(self):
        super().__init__(width, height, "Bouncing Balls!!")
        self.balls = []
        ball = Ball.createBall(random.randint((10), (width - 10)), random.randint((10), (height - 10)))
        self.balls.append(ball)

    # special handler function for drawing (doesn't work if it's called "drawBalls" or something like that)
    def on_draw(self):
        # similar to pygame.init()
        arcade.start_render()

        for ball in self.balls:
            arcade.draw_circle_filled(ball.x, ball.y, ball.size, ball.colour)

    # similar special handler function for updating objects (needs delta_time argument, doesn't work otherwise)
    #uses physics engine
    def on_update(self, delta_time):
        for ball in self.balls:
            ball.x += ball.dx
            ball.y += ball.dy

            # hitting walls (takes into account ball width so it doesn't half-disappear)
            # if ball hits left side of the screen
            if ball.x < ball.size:
                ball.dx *= -1

            # if ball hits top of screen
            if ball.y < ball.size:
                ball.dy *= - 1

            # if ball hits right side of screen
            if ball.x > width - ball.size:
                ball.dx *= -1
            
            # if ball hits bottom of screen
            if ball.y > height - ball.size:
                ball.dy *= - 1

     # special handler for mouse clicks (button is button that is pressed, modifiers are all keys like shift/ctrl pressed )
    def on_mouse_press(self, x, y, button, modifiers):
        ball = Ball.createBall(x, y)
        self.balls.append(ball)

    # almost the same as on_mouse_press but with keys instead of buttons
    def on_key_press(self, key, modifiers):
        if key == arcade.key.DOWN:
            self.balls.pop()
        if key == arcade.key.UP:
            ball = Ball.createBall(random.randint((10), (width - 10)), random.randint((10), (height - 10)))
            self.balls.append(ball)

    def on_mouse_motion(self, x, y, dx, dy):
        for ball in self.balls:
            ball.x = x
            ball.y = y 

def main():
    ballGame()
    arcade.run()

main()

