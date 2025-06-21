from player import Player
from game import Game

class Match:
    def __init__(self, player1, player2, games_to_win=3):
        self.player1 = player1
        self.player2 = player2
        self.games_to_win = games_to_win
        self.current_game = Game(player1, player2)
        self.game_history = []