from game import start_game

def menu():
    print("================= MENU =================")
    print("1) PLAY.")
    print("2) SCORE TABLE.")
    print("3) EXIT.")
    res = int( input("Seleccion: ") )

    if res == 1:
        game_screen()
    elif res == 2:
        score_screen()
    else:
        return


def game_screen():
    start_game()

def score_screen():
    print("SCORE TABLE")

menu()