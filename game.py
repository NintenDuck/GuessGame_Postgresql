import random
from enum import Enum
from clear_screen import cls
# ============================================================== #

class game_status( Enum ):
    STARTING    = 1
    PLAYING     = 2
    ENDED       = 3
    VICTORY     = 4
    GAMEOVER    = 5

class Game:
    def __init__(self, secret_range=5, debug=False) -> None:
        self.debug = debug
        self.secret_range = secret_range
        self.secret_number = self._get_new_secret()
        self.user_selection = self.secret_range+1
        self.game_state = game_status.STARTING
    
    def start( self ):
        cls()
        print("Game Started!!!")
        self._init()
        self._game()
    
    def _init( self ):
        pass

    def _game( self ):
        pass
    
    def _get_new_secret( self ):
        secret_num = random.randrange( -self.secret_range, self.secret_range )
        return secret_num

    # GETTERS
    def _get_secret_number( self ):
        return self.secret_number
    def _get_user_selection( self ):
        return self.user_selection