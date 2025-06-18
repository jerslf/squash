class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_won = 0
    
    def reset_score(self):
        self.score = 0
    
    def add_point(self):
        self.score += 1
    
    def remove_point(self):
        self.score -= 1
    
    def won_game(self):
        self.games_won += 1


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.max_score = 11
        self.current_game_score = (0, 0)

    def update_current_game_score(self):
        self.current_game_score  = (self.player1.score, self.player2.score)   

    def point_won_by(self, player):
        # Add point to player 1 or 2
        if player == self.player1:
            self.player1.add_point()
        elif player == self.player2:
            self.player2.add_point()
        # Update current_game_score
        self.update_current_game_score()

    
    


class Match:
    def __init__(self, player1, player2, games_to_win):
        pass