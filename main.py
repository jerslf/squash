from player import Player
from match import Match
from game import Game
from scoreboard import Scoreboard

def create_players():
    """Prompts the user to enter names for the two players."""
    p1_name = input("Enter name for Player 1: ")
    p2_name = input("Enter name for Player 2: ")
    
    # Use provided names, or default if none are given
    player1 = Player(p1_name if p1_name else "Player A")
    player2 = Player(p2_name if p2_name else "Player B")
    
    print(f"\nMatch: {player1.name} vs {player2.name}. Best of 5 games.")
    input("Press Enter to start...")
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
        command = input("\nEnter command: ").strip()

        match command:
            case "1":
                match.won_point(match.player1)
            case "2":
                match.won_point(match.player2)
            case "u1":
                match.remove_point(match.player1)
            case "u2":
                match.remove_point(match.player2)
            case "l":
                match.serve.set_serve_side("Left")
            case "r":
                match.serve.set_serve_side("Right")
            case "RE":
                confirm = input("Are you sure you want to reset the match? (y/N): ")
                if confirm.lower() == 'y' or confirm.lower() == "yes":
                    match = Match(player1, player2)
                    scoreboard = Scoreboard(match)
            case "q":
                print("Exiting match.")
                break
            case _:
                print("Invalid input, please try again.")
                input("Press Enter to continue...")
        

if __name__ == "__main__":
    main()