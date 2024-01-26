import os
import datetime
import random


class RPSGame:
    """
    Rock, Paper, Scissors Game Class. 

    Attributes:
        seed: int - the seed value for the random number generator

    Methods:
        set_random_seed(seed: int) -  
    """
    player_wins = []
    player_hist = []
    computer_hist = []

    victory_matrix = {
        "S": {
            "R": 1,
            "S": 0,
            "P": -1,
        },
        "R": {
            "R": 0,
            "S": -1,
            "P": 1,
        },
        "P": {
            "R": -1,
            "S": 1,
            "P": 0,
        },
    }

    def __init__(self, player_name: str, computer_name: str = None, seed: int=None, *args, **kwargs) -> None:
        self.player_name = player_name
        if computer_name is None:
            computer_name = "Winston"
        self.computer_name = computer_name
        self.set_random_seed(seed)

    def set_random_seed(self, seed: int|None) -> None:
        self.seed = seed
        random.seed(seed)

    def _test_random(self, N: int = 5):
        results = []
        for _ in range(N):
            results.append(round(random.random()*1000,0))
        print(results)

    def play_match(self, player_choice: str = None):

        valid_choices = ["R", "P", "S"]
        if player_choice is None:
            player_choice = input(f"What is your choice {valid_choices}: ").upper()
        
        comp_choice = random.choice(valid_choices)

        print(f"You have chosen {player_choice}")
        if player_choice not in valid_choices:
            print("You have chosen poorly. You lose. Read directions next time.")

        elif self.victory_matrix[player_choice][comp_choice] > 0:
            print("Computer beat you :(")

        elif self.victory_matrix[player_choice][comp_choice] == 0:
            print("You tied!")

        else:
            print("You win. The machines won't take over \U0001f600")

    def __str__(self) -> str:
        d = {
            "PC Name": self.computer_name,
            "seed": self.seed,
            "Player Name": self.player_name,
        }
        return f"{d}"
    

if __name__ == "__main__":
    print("Testing an initial game with no seed.")
    G1 = RPSGame(player_name="Shadin")
    # G2 = RPSGame(player_name="Shadin", seed=42, computer_name="James")

    G1.play_match("S")
    # print("G2:", G2)
