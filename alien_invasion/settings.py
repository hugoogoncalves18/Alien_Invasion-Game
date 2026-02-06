class Settings():
    def __init__(self):
        """Inicializa as configurações estáticas do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Configurações da espaçonave
        self.ship_limit = 3
        # Configurações dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Configurações dos alienígenas
        self.fleet_drop_speed = 10
        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1  # ← Isso será usado para aumentar dificuldade
        self.score_scale = 1.5
        # Inicializa as configurações que mudam durante o jogo
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self): #Inicia as configurações que alteram o jogo
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self): #Aumenta a velocidade do jogo
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
    