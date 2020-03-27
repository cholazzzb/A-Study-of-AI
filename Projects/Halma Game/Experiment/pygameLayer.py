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

class Actor(pygame.sprite.Sprite):
    def __init__(self, group, color, layer, pos, size):
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self._layer = layer
        pygame.sprite.Sprite.__init__(self, group)

# class ActorText(pygame.sprite.Sprite):
#     def __init__(self, group, color, layer, pos, size, text):
#         self.image = pygame.Surface(size)
#         self.image.fill(color)
#         self.rect = self.image.get_rect(center=pos)
#         self._layer = layer
#         pygame.sprite.Sprite.__init__(self, group)    

class Text(pygame.sprite.Sprite):
    def __init__(self, group, text, size, color, width, height, layer):
        # Call the parent class (Sprite) constructor  
        # pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        self._layer = layer
        
        pygame.sprite.Sprite.__init__(self, group)


group = pygame.sprite.LayeredUpdates()
Actor(group, (255, 255, 255), -5, (100, 100), (30, 30))
Actor(group, (255, 0, 255),   1, (110, 110), (50, 30))
Actor(group, (0, 255, 255),   0, (120, 120), (30, 30))
Actor(group, (255, 255, 0),   3, (130, 130), (30, 30))
Actor(group, (0, 0, 255),     2, (140, 140), (30, 30))
Text(group, "Coba", 10, blue, 40, 40, 3)

## Code tambahan atau tester
fontSmall = pygame.font.Font('freesansbold.ttf', 16)
tPlayer1 = fontSmall.render('PLAYER1', True, green, blue) #(the text, True, text colour, background color)
tPlayer1R = tPlayer1.get_rect() 
tPlayer1R.center = (100, 100) 

run = True
while run:
    for e in pygame.event.get():
        if e.type ==pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    screen.blit(tPlayer1, tPlayer1R)
    group.update()
    group.draw(screen)
    pygame.display.flip()