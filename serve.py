from player import Player

class Serve:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.server = player1
        self.side = "Right"
        self.hand_out = True
        self.indicator = "●"
    
    def handout(self):
        if self.server == self.player1:
            self.server = self.player2
        else:
            self.server = self.player1
        
        self.hand_out = True

    def set_serve_side(self, side):
        self.side = side
    
    def alternate_side(self):
        if self.side == "Left":
            self.side = "Right"
        else:
            self.side = "Left"
        
        self.hand_out = False
    
    def __str__(self):
        return (
            f"Server: {self.server.name}\n"
            f"Side: {self.side}\n"
            f"Hand Out: {self.hand_out}\n"
        )