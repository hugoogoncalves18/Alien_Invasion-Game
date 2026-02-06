import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #cria um retângulo para o projetil em 0,0
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y) #Amazena a posição do projetil como um valor decimal
        self.color = ai_settings.bullet_color #define a cor
        self.speed_factor = ai_settings.bullet_speed_factor #define a velocidade
    def update(self):
        self.y -= self.speed_factor #atualiza a posição do projetil
        self.rect.y = self.y #atualiza a posição do retângulo
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect) #desenha o retângulo