import pygame, random
from sys import exit
from button import Button, FlatButton

class Window:
    def __init__(self, screen_width: int, screen_height: int, FPS: int, caption: str):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.caption = caption
        self.FPS = FPS
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("wordlix/font/game.ttf", 30)

        self.BG = pygame.image.load("wordlix/images/bg/bg.png")

        self.screen = pygame.display.set_mode((self.screen_width, screen_height))
        pygame.display.set_caption(self.caption)

    def scale_image_percent(self, image, percent):
        width = int(image.get_width() * (percent / 100))
        height = int(image.get_height() * (percent / 100))
        return pygame.transform.scale(image, (width, height))

    def menu_loop(self):
        run = True
        
        while run:
            self.MOUSE_POS = pygame.mouse.get_pos()
            self.screen.blit(self.BG, (0, 0))

            text_boton = FlatButton((540, 100), (90, 10, 200), (212, 240, 111), (90, 70), self.screen, None, 'a', self.font)
            
            menu_font = pygame.font.Font("wordlix/font/game.ttf", 50)
            MENU_TEXT = menu_font.render("Tutti  Frutti", True, "black")
            MENU_RECT = MENU_TEXT.get_rect(center = (540, 70))
            sub_menu_font = pygame.font.Font("wordlix/font/game.ttf", 20)
            SUB_MENU_TEXT = sub_menu_font.render("guessing", True, "black")
            SUB_MENU_RECT = SUB_MENU_TEXT.get_rect(center = (540, 110))

            PLAY_BT = Button(None, (540, 242), 'Jugar', self.font, "Black", "blue", self.screen)
            OPTIONS_BT = Button(None, (540, 302), 'Opciones', self.font, "Black", "cyan", self.screen)
            QUIT_BT = Button(None, (540, 362), 'Salir', self.font, "Black", "Red", self.screen)
            
            for button in [PLAY_BT, OPTIONS_BT, QUIT_BT, text_boton]:
                button.changeColor(self.MOUSE_POS)
                button.update()

            self.screen.blit(MENU_TEXT, MENU_RECT)
            self.screen.blit(SUB_MENU_TEXT, SUB_MENU_RECT)

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
                    exit()
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        run = False
                        exit()
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BT.IsPressed(self.MOUSE_POS):
                        self.play_loop()
                    if OPTIONS_BT.IsPressed(self.MOUSE_POS):
                        self.options_loop()
                    if QUIT_BT.IsPressed(self.MOUSE_POS):
                        run = False
                        exit()

            self.clock.tick(self.FPS)
            pygame.display.update()
    
    def options_loop(self):
        run = True
        
        while run:
            self.MOUSE_POS = pygame.mouse.get_pos()
            self.screen.blit(self.BG, (0, 0))

            options_font = pygame.font.Font("wordlix/font/game.ttf", 50)
            MENU_TEXT = options_font.render("Opciones", True, "black")
            MENU_RECT = MENU_TEXT.get_rect(center = (540, 60))

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
                    exit()
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        run = False
                        self.menu_loop()

            self.clock.tick(self.FPS)
            pygame.display.update()

    def play_loop(self):
        run = True

        while run:
            self.MOUSE_POS = pygame.mouse.get_pos()
            self.screen.blit(self.BG, (0, 0))

            play_font = pygame.font.Font("wordlix/font/game.ttf", 50)
            MENU_TEXT = play_font.render("Sala", True, "black")
            MENU_RECT = MENU_TEXT.get_rect(center = (540, 60))

            CREATE_PARTY_BT = Button(None, (200, 170), 'Crear', self.font, 'black', 'green', self.screen)
            JOIN_PARTY_BT = Button(None, (200, 240), 'Unirse', self.font, 'black', 'blue', self.screen)
            BACK_BT = Button(None, (200, 310), 'Salir', self.font, 'black', 'red', self.screen)

            for button in [BACK_BT, CREATE_PARTY_BT, JOIN_PARTY_BT]:
                button.changeColor(self.MOUSE_POS)
                button.update()

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
                    exit()
                if self.event.type == pygame.KEYDOWN:
                    if self.event.key == pygame.K_ESCAPE:
                        run = False
                        self.menu_loop()
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BT.IsPressed(self.MOUSE_POS):
                        run = False
                        self.menu_loop()

            self.clock.tick(self.FPS)
            pygame.display.update()

    def update(self):
        self.menu_loop()