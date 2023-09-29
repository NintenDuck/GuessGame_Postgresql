import psycopg2
import json

class DataBaseConnection:
    def __init__(self, ip, port, user, password) -> None:
        pass

def get_secret( column_name="" ):
    with open( "secret_keys.json", "r" ) as file:
        data = json.load(file)
        return data[column_name]