import random
from enum import Enum
from .score_add_menu import show_add_score_menu
from clear_screen import cls
# ============================================================== #

class game_status( Enum ):
    IDLE        = 0
    STARTING    = 1
    PLAYING     = 2
    ENDED       = 3
    VICTORY     = 4
    GAMEOVER    = 5

class Game:
    def __init__(self, guess_range=5, debug=False) -> None:
        self._debug = debug
        self._guess_range = guess_range
        self._secret_number = 0
        self._user_selection = 0
        self._game_state = game_status.IDLE
    
    def start( self ):
        cls()
        print("Game Started!!!")
        self._init()
        self._game()
    
    def _init( self ):
        self._game_state = game_status.STARTING
        self._secret_number = self._get_new_secret()
        self._user_selection = self._secret_number + 1

    def _game( self ):
        first_round = True
        user_tries = 0

        while self._game_state != game_status.ENDED:
            cls()
            if self._get_debug():
                print(">>> Psssst!, the secret number is", self._get_secret_number())
            print("GUESS THE NUMBER BETWEEN -{0} and {0}".format(self._guess_range))
            print("\t\t\tTries:", user_tries)
            if not first_round:
                print("Your last guess was:", self._get_user_selection())
                if self._get_user_selection() > self._get_secret_number():
                    print("A little lower big boy")
                else:
                    print("A little bit higher cowboy")

            new_selection = int( input( "Your guess: " ) )
            self._set_user_selection( new_selection )

            if self._get_user_selection() == self._get_secret_number():
                self._victory_screen( user_tries+1 )
                self._set_game_state( game_status.ENDED )
            
            user_tries += 1
            first_round = False

    
    def _get_new_secret( self ):
        secret_num = random.randrange( -self._guess_range, self._guess_range )
        return secret_num

    def _victory_screen( self, final_score ):
        cls()
        print("You Win!!!")
        print("Final score:", final_score )
        input("Press any key...")
        show_add_score_menu( final_score )
        self._continue()

    def _continue( self ):
        cls()
        print("Want to play again? (y/n)")
        res = input("> ")
        if res.lower() == "y":
            self.start()
        elif res.lower() == "n":
            print("Hope to see you again soon human!!!")
            print("Exiting program...")
        else:
            self._continue()

        
    # GETTERS
    def _get_secret_number( self ):
        return self._secret_number
    def _get_user_selection( self ):
        return self._user_selection
    def _get_game_state( self ):
        return self._game_state
    def _get_debug( self ):
        return self._debug

    # SETTERS
    def _set_user_selection( self, new_selection ):
        self._user_selection = new_selection
    def _set_game_state( self, new_state ):
        self._game_state = new_state