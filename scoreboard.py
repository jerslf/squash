def display_scoreboard(player1, player2):
    print(f"\n{'SCOREBOARD':^30}")
    print("-" * 30)
    print(f"{player1.name:<15}{player1.score:>5}")
    print(f"{player2.name:<15}{player2.score:>5}")
    print("-" * 30 + "\n")