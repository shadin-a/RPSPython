import os
import datetime
import random


def logtime(format: str = "%Y-%m-%d %H_%M_%S"):
    """
    Parameters:
        format: str - Datetime string format.
    Returns the current datetime in a string format
    """
    return datetime.datetime.now().strftime(format)


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

    game_start = logtime()

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

    # Name a logging directory
    

    def __init__(self, player_name: str, computer_name: str = None, seed: int=None, logpath: str = None, *args, **kwargs) -> None:
        if logpath is None:
            self.LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game_logs")
        else:
            self.LOG_PATH = logpath
        
        if not os.path.exists(self.LOG_PATH):
            os.makedirs(self.LOG_PATH)
        
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

        if player_choice not in valid_choices:
            print("You have chosen poorly. You lose. Read directions next time.")
            return

        elif self.victory_matrix[player_choice][comp_choice] > 0:
            print("Computer beat you :(")
            self.player_wins.append("L")

        elif self.victory_matrix[player_choice][comp_choice] == 0:
            print("You tied!")
            self.player_wins.append("T")

        else:
            print("You win. The machines won't take over \U0001f600")
            self.player_wins.append("W")

        self.player_hist.append(player_choice)
        self.computer_hist.append(comp_choice)
    
    def write_logs(self, filename: str=None, sep: str=","):
        if filename is None:
            filename = f"{self.game_start}_log.txt"
        
        with open(os.path.join(self.LOG_PATH, filename), "w") as f:
            f.write(f"{sep.join(['MatchNumber', 'PlayerWins', 'PlayerChoice', 'ComputerChoice'])}\n")
            for row_num, row in enumerate(zip(self.player_wins, self.player_hist, self.computer_hist)):
                f.write(f"{str(row_num+1) + sep + sep.join(row)}\n")

    def __str__(self) -> str:
        d = {
            "PC Name": self.computer_name,
            "seed": self.seed,
            "Player Name": self.player_name,
        }
        return f"{d}"
    

if __name__ == "__main__":
    G1 = RPSGame(player_name="Shadin")

    for _ in range(50):
        G1.play_match("S")
    
    print(G1.player_wins)
    G1.write_logs()
