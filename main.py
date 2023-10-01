from sources.game.game_menu import Game
from sources.score_table.score_menu import show_table
from sources.databases.db_manager import add_score
from clear_screen import cls

debug = True

def menu():
    
    res = 0
    while res != 3:
        cls()
        print("================= MENU =================")
        print("1) PLAY.")
        print("2) SCORE TABLE.")
        print("3) EXIT.")
        if debug:
            print("4) DEBUG FUNCTION")
        res = int( input("Selection: ") )

        if res == 1:
            new_game = Game( 5, debug )
            new_game.start()
        elif res == 2:
            show_table()
        elif res == 4 and debug:
            cls()
            print("No Method assigned!!!")
            input("Press any key to continue...")
        else:
            return


if __name__ == "__main__":
    menu()