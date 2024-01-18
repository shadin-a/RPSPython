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
BASE_PATH = os.path.dirname(
        os.path.abspath(__file__)
    )

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
valid_choices = ['R', 'P', 'S']

def test_randoms(N: int = 1000) -> dict:
    cchoice = {key: 0 for key in valid_choices}
    for _ in range(N):
        comp_choice = random.choice(valid_choices)
        cchoice[comp_choice] += 1

    for key in cchoice:
        cchoice[key] = cchoice[key]/N

    return cchoice


with open(os.path.join(LOG_PATH, f"gamelog_{logtime()}.txt"), "w") as f:
    f.write("TESTING LOG for RANDOMNESS \n")
    f.write(f'{"-"*20}\n')
    f.write(f"{test_randoms()}\n\n")
    f.write("END OF TESTING")