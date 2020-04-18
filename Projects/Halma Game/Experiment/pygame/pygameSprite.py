import pygame

black = (0, 0, 0)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pygame.init()
screen = pygame.display.set_mode((300, 300))
 
class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, size, color, width, height):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])

# class Text(pygame.sprite.Sprite):
#     def __init__(self, text, size, color, font=None, **kwargs):
#         super(Text, self).__init__()
#         self.color = color
#         self.font = pygame.font.Font(font, size)
#         self.kwargs = kwargs
#         self.set(text)

#     def set(self, text):
#         self.image = self.font.render(str(text), 1, self.color)
#         self.rect = self.image.get_rect(**self.kwargs)

group = pygame.sprite.LayeredUpdates()
Text(group, "Coba", 36, blue, 60, 60)

## Code tambahan atau tester
# fontSmall = pygame.font.Font('freesansbold.ttf', 16)
# tPlayer1 = fontSmall.render('PLAYER1', True, green, blue) #(the text, True, text colour, background color)
# tPlayer1R = tPlayer1.get_rect() 
# tPlayer1R.center = (100, 100) 

run = True
while run:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    # screen.blit(tPlayer1, tPlayer1R)
    group.update()
    group.draw(screen)
    pygame.display.flip()