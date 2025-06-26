from player import Player
from match import Match
from game import Game
from scoreboard import Scoreboard

def create_players():
    player1 = Player("Jeremy")
    player2 = Player("Alex")
    return player1, player2

def main():
    player1, player2 = create_players()
    match = Match(player1, player2)
    scoreboard = Scoreboard(match)

    # Main loop
    while True:
        # Update the display every time a point is scored
        scoreboard.update_display()
        
        # Handle match completion
        if match.is_finished:
            print(f"MATCH FINISHED. {match.winner.name} WON")
            break
        
        # Handle command
        command = input("\nEnter command: ").lower().strip()

        if command == "1":
            match.won_point(match.player1)
        elif command == '2':
            match.won_point(match.player2)
        elif command == 'u1':
            match.remove_point(match.player1)
        elif command == 'u2':
            match.remove_point(match.player2)
        elif command == 'r':
            confirm = input("Are you sure you want to reset the match? (y/N): ")
            if confirm.lower() == 'y':
                match = Match(player1, player2)
                scoreboard = Scoreboard(match)
        elif command == 'q':
            print("Exiting match.")
            break
        else:
            print("Invalid input, please try again.")
            input("Press Enter to continue...")
        

if __name__ == "__main__":
    main()