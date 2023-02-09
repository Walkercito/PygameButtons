import pygame

class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, screen):
        self.screen = screen
        self.image = image
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.font = font
        self.text_input = text_input
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        self.text_rect = self.text.get_rect(center = (self.pos_x, self.pos_y)) 

    def update(self):
        if self.image is not None:
            self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)
    
    def IsPressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

#·-------------------------------------------------------------------------------------------------------------------------------------------·#

class FlatButton:
    def __init__(self, pos: tuple, base_color: tuple, hovering_color: tuple, size: tuple, screen, image = None, input_text = None, font = None):
        self.screen = screen
        self.text_input = input_text
        self.font = font
        self.size = size
        self.image = image
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.base_color, self.hovering_color = base_color, hovering_color
        if self.text_input is not None:
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            self.text_rect = self.text.get_rect(center = (self.pos_x, self.pos_y)) 
        if self.image is None:
            self.image = pygame.Surface((self.size))
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))

    def update(self):
        self.screen.blit(self.image, self.rect)
        if self.text_input is not None:
            self.screen.blit(self.text, self.text_rect)

    def IsPressed(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = pygame.Surface(self.size)
            self.image.fill(self.hovering_color)
            if self.text_input:
                if self.text_input is not None:
                    self.text = self.font.render(self.text_input, True, self.base_color)
                    self.screen.blit(self.text, self.text_rect)
        else:
            self.image = pygame.Surface(self.size)
            self.image.fill(self.base_color)
            if self.text_input:
                if self.text_input is None:
                    self.text = self.font.render(self.text_input, True, self.hovering_color)
                    self.screen.blit(self.text, self.text_rect)