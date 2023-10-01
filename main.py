from game_menu import Game
from score_menu import show_table
from databases.db_manager import add_score

debug = True

def menu():
    # TODO: MAKE MENU CYCLE UNTIL OTHER ACTION
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
        print("No Method assigned!!!")
    else:
        return


if __name__ == "__main__":
    menu()