import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings , screen): #Inicia a aeronave e define a posição inicial
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp') #Carrega a imagem da aeronave
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx #Posiciona a aeronave no centro da tela
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False #flag de movimento
        self.moving_left = False #flag de movimento
    def update(self): #Atualiza conforme a flag de movimento
        if self.moving_right and self.rect.right < self.screen_rect.right: #São colocados os valores de > e < para limitar a nave a não sair da tela
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self): #Desenha a aeronave na tela
        self.screen.blit(self.image, self.rect)
    def center_ship(self): #Coloca a aeronave no centro da tela
        self.center = self.screen_rect.centerx