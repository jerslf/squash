from player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.max_score = 11
        self.game_score = (0, 0)

    def update_game_score(self):
        self.game_score  = (self.player1.score, self.player2.score)   

    def won_point(self, player):
        # Add point to player 1 or 2
        if player == self.player1:
            self.player1.add_point()
        elif player == self.player2:
            self.player2.add_point()
        # Update current_game_score
        self.update_game_score()
    
    def is_over(self):
        p1, p2 = self.player1.score, self.player2.score
        return (p1 >= self.max_score or p2 >= self.max_score) and abs(p1 - p2) >= 2