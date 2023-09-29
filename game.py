import random
from enum import Enum
# ============================================================== #

class game_status( Enum ):
    STARTING    = 1
    PLAYING     = 2
    ENDED       = 3
    VICTORY     = 4
    GAMEOVER    = 5

secret_number = 0
user_selection = 0

def start_game():
    print("===== GAME START! =====")
    _init()
    _game()

def _init():
    # TODO: FIX CANNOT ACCESS LOCAL VARIABLES
    secret_number = get_rand_number()
    if user_selection == secret_number:
        user_selection += 1

def _game():
    state = game_status.STARTING
    while state != game_status.ENDED:
        pass

def get_rand_number():
    return random.randrange(-10,10)