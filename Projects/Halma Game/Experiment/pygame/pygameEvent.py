import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((900,500))
pygame.display.set_caption('Test')

pygame.display.update()

Loop = True

while Loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Loop = False


pygame.quit()
quit()