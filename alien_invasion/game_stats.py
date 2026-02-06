class GameStats():
    def __init__(self, ai_settings):
        self.high_score = 0
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
    def reset_stats(self): #inicia os dados estatisticos que podem ser alterados durente o jogo
        self.ships_left = self.ai_settings.ship_limit # Criaremos uma instância de GameStats que será usada durante todo o tempo que a Invasão Alienígena executar
        self.score = 0
        self.level = 1