def display_scoreboard(player1, player2, game_history):
    print("\n🎾 MATCH SCOREBOARD 🎾")
    print("+-----------------+--------+------+------+------+------+------+")
    print("| Player          | Games  | G1   | G2   | G3   | G4   | G5   |")
    print("+-----------------+--------+------+------+------+------+------+")

    def format_row(player, is_player1):
        row = f"| {player.name:<15} |  {player.games_won:^5} |"
        for i in range(5):
            if i < len(game_history):
                score = game_history[i][0] if is_player1 else game_history[i][1]
                row += f" {score:^4} |"
            else:
                row += "      |"
        return row

    print(format_row(player1, is_player1=True))
    print(format_row(player2, is_player1=False))
    print("+-----------------+--------+------+------+------+------+------+\n")