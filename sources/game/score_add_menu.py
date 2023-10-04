from sources.databases.db_manager import add_score
from clear_screen import cls

def show_add_score_menu( final_score=-1):
    cls()
    if final_score == -1:return
    correct_username = False
    user_name = ""
    
    while correct_username == False:
        print("Tell me your name so i can register it!")
        user_name = input("R: ")
        add_score( user_name, final_score )

        if user_name != "":
            correct_username = True
        cls()

    print("Score added succesfully!!!")
    input("Press any key to continue...")