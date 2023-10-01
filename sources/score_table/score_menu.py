from clear_screen import cls
from sources.databases.db_manager import get_score_table
from enum import Enum


def show_table():
    cls()
    score_table = get_score_table()
    print("\tRANKINGS")
    print("__________________________________")
    print("NAME\t\t\tSCORE")
    print("__________________________________")
    for score in score_table:
        print( score[1], "\t\t\t", score[2] )
    
    input("Press any key to return...")