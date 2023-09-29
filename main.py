numero_secreto = 0

def menu():
    print("================= MENU =================")
    print("1) PLAY.")
    print("2) SCORE TABLE.")
    print("3) EXIT.")
    res = int( input("Presiona cualquier letra...") )

    if res == 1:
        game_screen()
    elif res == 2:
        score_screen()
    else:
        return


def game_screen():
    print("GAME SCREEN")

def score_screen():
    print("SCORE TABLE")

menu()