from game_menu import Game
from score_menu import show_table


debug = True

def menu():
    # TODO: MAKE MENU CYCLE UNTIL OTHER ACTION
    print("================= MENU =================")
    print("1) PLAY.")
    print("2) SCORE TABLE.")
    print("3) EXIT.")
    res = int( input("Selection: ") )

    if res == 1:
        new_game = Game( 5, True )
        new_game.start()
    elif res == 2:
        show_table()
    else:
        return


menu()