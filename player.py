class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.games_won = 0
    
    def add_point(self):
        self.score += 1
    
    def remove_point(self):
        if self.score > 0:
            self.score -= 1
    
    def won_game(self):
        self.games_won += 1
    
    def reset_score(self):
        self.score = 0

    def reset_match(self):
        self.score = 0
        self.games_won = 0
    
    def __str__(self):
        return f"{self.name} ({self.games_won} games)"