from player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.max_score = 11
        self.game_score = (0, 0)
        self.is_finished = False
        self.winner = None

    def update_game_score(self):
        self.game_score  = (self.player1.score, self.player2.score)   

    def won_point(self, player):
        """Add point to specified player and check if game is over"""
        if self.is_finished:
            return
        
        if player == self.player1:
            self.player1.add_point()
        elif player == self.player2:
            self.player2.add_point()
        
        self.update_game_score()

        if self.is_over():
            self.finish_game()
        return True
    
    def remove_point(self, player):
        """Remove point from specified player and check if game is over"""
        if self.is_finished:
            return
        
        if player == self.player1:
            self.player1.remove_point()
        elif player == self.player2:
            self.player2.remove_point()
        
        self.update_game_score()
        return True
    
    def is_over(self):
        """Return True if player wins game by 2 points"""
        p1, p2 = self.player1.score, self.player2.score
        return (p1 >= self.max_score or p2 >= self.max_score) and abs(p1 - p2) >= 2
    
    def finish_game(self):
        """Mark game as finished and determine winner"""
        if not self.is_over:
            return False
        
        self.is_finished = True
        if self.player1.score > self.player2.score:
            self.winner = self.player1
            self.player1.won_game()
        else:
            self.winner = self.player2
            self.player2.won_game()
        
        return True