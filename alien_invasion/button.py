import pygame.font

class Button():
    def __init__(self, ai_settings, screen, msg): #Inicia os atributos do botão
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = 200, 50 #Define as dimensões e propriedades do botão
        self.button_color = (0, 255, 0) #Define a cor do botão
        self.text_color = (255, 255, 255) #Define a cor da letra
        self.font = pygame.font.SysFont(None, 48) #Define o tamanho da letra
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center #Coloca o botão no centro da tela
        self.prep_msg(msg)
    def prep_msg(self, msg): #Prepara a mensagem para ser exibida no botão
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self): #Desenha o botão na tela
        self.screen.fill(self.button_color, self.rect) #Desenha o botão em branco
        self.screen.blit(self.msg_image, self.msg_image_rect) #Desenha a mensagem