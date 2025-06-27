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
        serve = self.match.serve
        # Add indicator and side to the server's display
        # Determine serve indicator
        if serve.side == "Left" and serve.hand_out == True:
            indicator  = serve.hand_out_left_indicator
        elif serve.side == "Right" and serve.hand_out == True:
            indicator  = serve.hand_out_right_indicator
        elif serve.side == "Left" and serve.hand_out == False:
            indicator  = serve.left_indicator
        else:
            indicator  = serve.right_indicator

       
        # Build display strings based on server
        if serve.server == self.match.player1:
            p1_display = f"{indicator} {self.match.player1.name} ({self.match.player1.games_won}) {self.match.player1.score}"
            p2_display = f"{self.match.player2.score} ({self.match.player2.games_won}) {self.match.player2.name}"
        else:
            p1_display = f"{self.match.player1.name} ({self.match.player1.games_won}) {self.match.player1.score}"
            p2_display = f"{self.match.player2.score} ({self.match.player2.games_won}) {self.match.player2.name} {indicator}"


        # Add 5 for padding and the separator between scores (3 for " - " and 2 for spaces)
        content_width = max(len(p1_display) + len(p2_display) + 5, 20)  # minimum width of 20
        
        print("\nSQUASH MATCH SCOREBOARD - BEST OF 5\n")
        print("+" + "-" * content_width + "+")
        print(f"| {p1_display} - {p2_display} |")
        print("+" + "-" * content_width + "+\n")

    def display_controls(self):
        """Display control instructions"""
        print("-" * 40)
        print("SCORING:")
        print(f"1  - Point to {self.match.player1.name}")
        print(f"2  - Point to {self.match.player2.name}")
        print(f"U1 - Remove last point from {self.match.player1.name}")
        print(f"U2 - Remove last point from {self.match.player2.name}")
        print()
        print("SERVE:")
        print("L  - Serving from Left")
        print("R  - Serving from Right")
        print(f"S1  - {self.match.player1.name} serving")
        print(f"S2  - {self.match.player2.name} serving")
        print()
        print("MATCH:")
        print("RESET - Reset match")
        print("Q  - Quit")
        print("-" * 40)
    
    def display_serve_info(self):
        print(self.match.serve)

    def update_display(self):
        """Update full scoreboard display"""
        self.clear_screen()
        self.display_controls()
        self.display_match_score()