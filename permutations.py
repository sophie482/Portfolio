#https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python

import pygame
from itertools import permutations

pygame.init()

def getPerms(wordToSolve):
    perms = [''.join(p) for p in permutations(wordToSolve)]
    number = 0
    permsOutput = ''
    for i in range(len(set(perms))):
        number +=1 
        permsOutput += str(perms[i])
    return(str(permsOutput) + "There are " + str(number) + " possible combinations.")

# def printPerms(wordToSolve):
#     for word in wordToSolve:
#         getPerms(wordToSolve)
#         wordToSolve = wordToSolve[:-1]


def main():
    screen = pygame.display.set_mode((700, 800))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    output_box = pygame.Rect(100, 175, 400, 400)
    WHITE = (255, 255, 255)
    colour = pygame.Color('lightskyblue3')
    text = ''
    output = ''
    done = False

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                        done = True  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        output = str(getPerms(text))
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else: 
                        text += event.unicode

        screen.fill(WHITE)
        # Render the current text.
        txt_surface = font.render(text, True, colour)
        output_surface = font.render(output, True, colour)

        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        output_width = max(300, output_surface.get_width()+10)
        output_box.w = output_width

        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        screen.blit(output_surface, (output_box.x+5, output_box.y+5))
        # screen.blit(screen, textBox(), (100, 200))

        # Blit the input_box rect.
        pygame.draw.rect(screen, colour, input_box, 2)
        pygame.draw.rect(screen, colour, output_box, 2)


        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
        
if __name__ == '__main__':
    main()
