from rps import RPSGame
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Rock-Paper-Scissors")


CORSMiddleware(app, allow_origin_regex="localhost")

def new_game(player_name: str="Billy Bob", random_seed: int=42):
    return RPSGame(player_name=player_name, seed=random_seed)

@app.get("/play-match")
def play_match(choice: str):
    choice = choice.upper()
    if choice not in ['S', 'R', 'P']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"message": "Choice parameter must be 'R', 'P', or 'S'"}
        )
    GAME = new_game()
    GAME.play_match(choice)

    return {
        "player_choice": GAME.player_hist[0],
        "player_wins": GAME.player_wins[0],
        "computer_choice": GAME.computer_hist[0],
    }