from player import Player

class Serve:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.server = player1
        self.side = "Right"
        self.hand_out = True

        self.left_indicator = "🅛"
        self.right_indicator = "🅡"
        self.hand_out_left_indicator = "🄻"
        self.hand_out_right_indicator = "🅁"
    
    def handout(self):
        if self.server == self.player1:
            self.server = self.player2
        else:
            self.server = self.player1
        
        self.hand_out = True
        self.side = "Right"

    def set_initial_server(self):
        print("Select initial server:")
        print(f"1 - {self.player1.name}")
        print(f"2 - {self.player2.name}")
        server_input = input("Enter 1 or 2: ").strip()
        if server_input == "1":
            self.server = self.player1
        elif server_input == "2":
            self.server = self.player2
        else:
            print("Invalid input. Defaulting to Player 1.")
            self.server = self.player1
            input("Press Enter to continue...")
    
    def change_server(self, player):
        self.server = player

    def set_serve_side(self, side):
        if side not in ["Left", "Right"]:
            raise ValueError("Side must be 'Left' or 'Right'")
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