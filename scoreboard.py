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
    
    def display_match_score(self):
        # Calculate the content width based on player names and scores
        p1_display = f"{self.match.player1.name} ({self.match.player1.games_won}) {self.match.player1.score}"
        p2_display = f"{self.match.player2.score} ({self.match.player2.games_won}) {self.match.player2.name}"
        # Add 5 for padding and the separator between scores (3 for " - " and 2 for spaces)
        content_width = max(len(p1_display) + len(p2_display) + 5, 20)  # minimum width of 20
        
        print("\nSQUASH MATCH SCOREBOARD - BEST OF 5\n")
        print("+" + "-" * content_width + "+")
        print(f"| {p1_display} - {p2_display} |")
        print("+" + "-" * content_width + "+\n")

    def display_controls(self):
        """Display control instructions"""
        print("CONTROLS:")
        print(f"1  - Point to {self.match.player1.name}")
        print(f"2  - Point to {self.match.player2.name}")
        print(f"u1 - Remove last point from {self.match.player1.name}")
        print(f"u2 - Remove last point from {self.match.player2.name}")
        print("r  - Reset match")
        print("q  - Quit")
        print()
        print("-" * 14)

    def update_display(self):
        """Update full scoreboard display"""
        self.clear_screen()
        self.display_match_score()
        self.display_controls()