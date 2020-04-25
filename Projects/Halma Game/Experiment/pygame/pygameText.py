import pygame
import sys

'''
CLUE : pygame will render new objek above the old objek
'''


class Score(object):
    def __init__(self):
        self.point = 0
        self.score_font = pygame.font.SysFont(None, 30)
        self.player1_score = self.score_font.render(str(self.point), True, black)

    def update(self):
        self.point += 1
        self.player1_score = self.score_font.render(str(self.point), True, black)

    def draw(self):
        screen.blit(self.player1_score, (100, 100))

pygame.init()
# clock = pygame.time.Clock()
fps = 60
size = [200, 200]
bg = [255, 255, 255]
red = (255, 0, 0)
black = (0, 0, 0)


screen = pygame.display.set_mode(size)


button = pygame.Rect(100, 100, 50, 50)  # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

font = pygame.font.SysFont(None, 25)
score = Score()


def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if button.collidepoint(pygame.mouse.get_pos()):
                print("mouse is over Button")
            else:
                print('mouse is not ')

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    score.update()


        screen.fill(bg)

        # first_text = font.render("FIRST", True, red)
        # screen.blit(first_text, [10, 10])
        pygame.draw.rect(screen, [255, 0, 0], button)  # draw button
        score.draw()
        pygame.display.update()
        # clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
    