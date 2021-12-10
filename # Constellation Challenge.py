# Constellation Challenge

import pygame
import random

pygame.init()

width = 500
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Constellation Challenge")
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
font = pygame.font.Font(None, 20)
stars = []


def drawInstructions():
    screen.fill(BLACK)
    text = font.render("Click on the canvas to form constellations!", True, WHITE)
    text2 = font.render("(Up arrow to add a random star, down arrow to delete the last star added.)", True, WHITE)
    screen.blit(text, [120, 25])
    screen.blit(text2, [25, 370])
    pygame.display.flip()
    Star.main()

class Star:
  def __init__(self, x, y, r, colour):
      self.x = x
      self.y = y
      self.r = r
      self.colour = colour

  def makeStar(self):
    pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r)
    pygame.display.flip()

  def connectTwoStars(starOne, starTwo):
    pygame.draw.line(screen, WHITE, (starOne.x, starOne.y), (starTwo.x, starTwo.y))

  def deleteStar(stars):
    stars.pop()

  def randomStar(stars):
    stars.append(Star((random.randint(0, width)), (random.randint(0, height)), 5, WHITE))


  def main():
    done = False
    clock = pygame.time.Clock()
    while not done:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            xMousePos = pos[0]
            yMousePos = pos[1]
            stars.append(Star(xMousePos, yMousePos, 5, WHITE))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                Star.deleteStar(stars)
            if event.key == pygame.K_UP:
                Star.randomStar(stars)

        screen.fill(BLACK)
        for i in range(len(stars)):
          Star.makeStar(stars[i])
          if (len(stars) > 1 and i + 1 < len(stars)):
            Star.connectTwoStars(stars[i], stars[i + 1])
        
    clock.tick(60)
    pygame.quit()

drawInstructions()