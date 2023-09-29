from game import Game

debug = True

def menu():
    print("================= MENU =================")
    print("1) PLAY.")
    print("2) SCORE TABLE.")
    print("3) EXIT.")
    res = int( input("Selection: ") )

    if res == 1:
        new_game = Game( 5, True )
        new_game.start()
    elif res == 2:
        score_screen()
    else:
        return

def score_screen():
    print("SCORE TABLE")

menu()