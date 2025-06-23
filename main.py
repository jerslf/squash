from player import Player
from match import Match
from game import Game
from scoreboard import display_scoreboard

def create_players():
    player1 = Player("Jeremy")
    player2 = Player("Alex")
    return player1, player2


def main():
    player1, player2 = create_players()
    game = Game(player1, player2)

    game.won_point(player1)
    display_scoreboard(player1, player2, game)

if __name__ == "__main__":
    main()