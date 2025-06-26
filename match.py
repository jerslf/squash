from player import Player
from game import Game
from serve import Serve

class Match:
    def __init__(self, player1, player2, games_to_win=3):
        self.player1 = player1
        self.player2 = player2
        self.games_to_win = games_to_win
        self.current_game = Game(player1, player2)
        self.game_history = []
        self.is_finished = False
        self.winner = None
        self.serve = Serve(player1, player2)

        # Reset players for new match
        self.player1.reset_match()
        self.player2.reset_match()
    
    def start_new_game(self):
        """Start a new game if current one is finished"""
        if self.is_finished:
            print("Can't start new game, match is finished")
            return False
        
        if self.current_game.is_finished:
            # Update game_history
            self.game_history.append(self.current_game)

            # Check if match is over
            if self.is_over():
                self.finish_match()
                return False
            
            # Start new game
            self.current_game = Game(self.player1, self.player2)
            return True

    def won_point(self, player):
        """Award point to player"""
        if self.is_finished:
            print("Can't award point, match is finished")
            return False
        
        self.current_game.won_point(player)

        # Handle Serve
        if player == self.serve.server:
            self.serve.alternate_side()
        else:
            self.serve.handout()

        # Check if we need to start a new game
        if self.current_game.is_finished:
            self.start_new_game()

        return True
    
    def remove_point(self, player):
        """Remove point from player"""
        if self.is_finished:
            return False
        return self.current_game.remove_point(player)
            
    def is_over(self):
        """Check if match is finished"""
        return self.player1.games_won >= self.games_to_win or self.player2.games_won >= self.games_to_win

    def finish_match(self):
        """Mark match as finished and determine winner"""
        if not self.is_over():
            return False
        
        self.is_finished = True
        if self.player1.games_won >= self.games_to_win:
            self.winner = self.player1
        else:
            self.winner = self.player2
        
        return True