from rps import RPSGame

print("Welcome to Rock Paper Scissors!\n")
GAME = RPSGame(player_name="Shadin")
while True:
    GAME.play_match()

    Continue = input("To quit the game, press 'Q': ").upper()
    if Continue == 'Q':
        break

GAME.write_logs(sep='|')