import pygame

class textBox(object):
    def __init__(self, positionX, positionY, width, height, colorText, colorUnhover, colorHover, font):

        self.positionX = positionX
        self.positionY = positionY
        self.width = width
        self.height = height
        self.textColor = colorText
        
        self.unhover = pygame.Surface((width, height))
        self.unhover.fill(colorUnhover)        

        self.hover = pygame.Surface((width, height))
        self.hover.fill(colorHover) 

        self.render = self.unhover

        self.font = font
        self.text = 0

    def draw(self, screen):
        self.renderedText = self.font.render(str(self.text), True, self.textColor)
        self.renderedTextBorder = self.renderedText.get_rect()
        self.renderedTextBorder.center = (self.positionX, self.positionY)

        screen.blit(self.render, (self.positionX-self.width/2, self.positionY-self.height/2))
        screen.blit(self.renderedText, self.renderedTextBorder)

    def updateText(self, newText):
        self.text = str(newText)

    def renderHover(self):
        self.render = self.hover

    def renderUnhover(self):
        self.render = self.unhover

    def isInsideTheButton(self, position):
        if position[0] > self.positionX and position[0] < self.positionX + self.width and position[1] > self.positionY and position[1] < self.positionY + self.height:
            return True
        else:
            return False