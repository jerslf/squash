from classes import Player, Game, Match
from scoreboard import display_scoreboard


def create_players():
    player1 = Player("Jeremy")
    player2 = Player("Alex")
    return player1, player2


def main():
    player1, player2 = create_players()
    match = Match(player1, player2)
    display_scoreboard(player1, player2, match.game_history)


if __name__ == "__main__":
    main()