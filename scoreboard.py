from player import Player
from game import Game
from match import Match
import sys

class Scoreboard:
    def __init__(self, match):
        self.match = match

    def clear_screen(self):
        """
        Clears the terminal screen and the scrollback buffer.
        """
        # \033[H: moves cursor to top-left
        # \033[2J: clears the viewport
        # \033[3J: clears the scrollback buffer
        print("\033[H\033[2J\033[3J", end="")
        sys.stdout.flush()
    
    '''def display_match_score(self):
        print("\n             SQUASH MATCH SCOREBOARD - BEST OF 5             ")
        print("+-----------------+--------+------+------+------+------+------+")
        print("| Player          |  Games |  G1  |  G2  |  G3  |  G4  |  G5  |")
        print("+-----------------+--------+------+------+------+------+------+")

        def format_row(player, is_player1):
            row = f"| {player.name:<15} |  {player.games_won:^5} |"
            for i in range(5):
                if i < len(self.match.game_history):
                    score = self.match.game_history[i][0] if is_player1 else self.match.game_history[i][1]
                    row += f" {score:^4} |"
                else:
                    row += "      |"
            return row

        print(format_row(self.match.player1, is_player1=True))
        print(format_row(self.match.player2, is_player1=False))
        print("+-----------------+--------+------+------+------+------+------+\n")'''
    
    def display_match_score(self):
        print("\nSQUASH MATCH SCOREBOARD - BEST OF 5\n")
        print("+-------------------------------+")
        print(f"| {self.match.player1.name} ({self.match.player1.games_won}) {self.match.player1.score} - {self.match.player2.score} ({self.match.player2.games_won}) {self.match.player2.name} |")
        print("+-------------------------------+\n")

    def display_controls(self):
        """Display control instructions"""
        print("CONTROLS:")
        print(f"1  - Point to {self.match.player1.name}")
        print(f"2  - Point to {self.match.player2.name}")
        print(f"u1 - Remove last point from {self.match.player1.name}")
        print(f"u2 - Remove last point from {self.match.player2.name}")
        print("r  - Reset match")
        print("q  - Quit")
        print("-" * 40)
    
    def display_serve_info(self):
        print(self.match.serve)

    def update_display(self):
        """Update full scoreboard display"""
        self.clear_screen()
        self.display_match_score()
        self.display_serve_info()
        self.display_controls()