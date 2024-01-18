import os
import datetime
import time
import random


def logtime(format: str = "%Y-%m-%d %H_%M_%S"):
    """
    Parameters:
        format: str - Datetime string format.
    Returns the current datetime in a string format
    """
    return datetime.datetime.now().strftime(format)


# Establish a base path to where this file is
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Name a logging directory
LOG_PATH = os.path.join(BASE_PATH, "game_logs")

print("Base Path:", BASE_PATH)
print("Log Path:", LOG_PATH)
print("runtime", logtime())

# time.sleep(3)
# print("runtime", logtime())

# If the logging directory doesn't exist
if not os.path.exists(LOG_PATH):
    # Create the log path
    os.mkdir(LOG_PATH)

# Create array for winners/losers
# puts a "P" for player win, "C" for computer win
winloss = []
# Create array for player choice
pchoice_hist = []
# Create an array for random computer choice
cchoice_hist = []
timeplayed = []

# valid choices for user input and computer selection
valid_choices = ["R", "P", "S"]


def test_randoms(N: int = 1000) -> dict:
    cchoice = {key: 0 for key in valid_choices}
    for _ in range(N):
        comp_choice = random.choice(valid_choices)
        cchoice[comp_choice] += 1

    for key in cchoice:
        cchoice[key] = cchoice[key] / N

    return cchoice


with open(os.path.join(LOG_PATH, f"gamelog_{logtime()}.txt"), "w") as f:
    f.write("TESTING LOG for RANDOMNESS \n")
    f.write(f'{"-"*20}\n')
    f.write(f"{test_randoms()}\n\n")
    f.write("END OF TESTING")


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

player_choice = input(f"What is your choice {valid_choices}: ").upper()


def play_match(player_choice):
    comp_choice = random.choice(valid_choices)

    print(f"You have chosen {player_choice}")
    if player_choice not in valid_choices:
        print("You have chosen poorly. You lose. Read directions next time.")

    elif victory_matrix[player_choice][comp_choice] > 0:
        print("Computer beat you :(")

    elif victory_matrix[player_choice][comp_choice] == 0:
        print("You tied!")

    else:
        print("You win. The machines won't take over \U0001f600")

play_match(player_choice)
