import pygame
import sys

#
from halma_view_gui_component import textBox    

black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = (0, 128, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode([600, 600])

isDisplayOn = True

font = pygame.font.Font('freesansbold.ttf', 15) # (font file, size)
fontSmall = pygame.font.Font('freesansbold.ttf', 10)

#
startButton = textBox(300, 300, 50, 50, black, white, grey, fontSmall)

testSurface = pygame.Surface((100, 100))
testSurface.fill(green)

testButton = textBox(50, 50, 10, 30, black, white, white, font)


while isDisplayOn:
    for event in pygame.event.get():

        mousePosition = pygame.mouse.get_pos()

        #
        if startButton.isInsideTheButton(mousePosition):
            startButton.renderHover()
        else:
            startButton.renderUnhover()
        
        #
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if startButton.isInsideTheButton(event.pos):
                print('button Pressed!')
                startButton.updateText(12)

        if event.type == pygame.QUIT:
            isDisplayOn = False

    #
    startButton.draw(screen)
    screen.blit(testSurface, (100,100))
    testButton.draw(testSurface)
    pygame.display.update()

pygame.quit()
sys.exit