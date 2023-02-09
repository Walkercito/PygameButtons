import pygame, random
from sys import exit

class Window:
    def __init__(self, screen_width: int, screen_height: int, FPS: int, caption: str):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.caption = caption
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("wordlix/font/game.ttf", 30)

        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        pygame.display.set_caption(self.caption)

    def scale_image_percent(self, image, percent):
        width = int(image.get_width() * (percent / 100))
        height = int(image.get_height() * (percent / 100))
        return pygame.transform.scale(image, (width, height))

    def main_loop(self):
        run = True
        
        while run:
            self.MOUSE_POS = pygame.mouse.get_pos()
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
                    exit()
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        run = False
                        exit()

            self.clock.tick(self.FPS)
            pygame.display.update()

            
    def update(self):
        self.menu_loop()
