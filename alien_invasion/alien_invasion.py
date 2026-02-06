import pygame #Funcionalidades dos jogos no Python
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game(): #Função para iniciar
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Cria a janela de exibição
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play") #Cria o botão Play
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group() #Cria um grupo de projéteis
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True: #Laço de eventos 
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)#inicia o laço principal do jogo
        if stats.game_active:
            ship.update() #atualiza a nave
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #print(len(bullets)) #teste de remoção de projeteis
        gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)#importa a função de atualização da tela
run_game() #Inicia o jogo e o laço principal