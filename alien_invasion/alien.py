import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen): #Inicia o alien e define a posição
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.bmp') #Carrega a imagem do alien
        self.rect = self.image.get_rect() #Define a posição do alien na parte superior esquerda da tela
        self.x = float(self.rect.x) #armazena a posição exata
        self.alien_speed_factor = 1
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

