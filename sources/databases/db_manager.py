import psycopg2
import json


def _get_secret_data( name="", secret_file="sources/databases/secret_keys.json" ) -> dict:
    with open( secret_file, "r" ) as file:
        data = json.load(file)
        return data[name]
        
def _connect_to_database( file_path="sources/databases/secret_keys.json" ):
    """Gets the connection and connection cursor as a dictionary

    Returns:
        dict: {'connection', 'cursor'}
    """
    connection = psycopg2.connect(
                                    dbname=_get_secret_data("db"),
                                    host=_get_secret_data("ip"),
                                    port=_get_secret_data("port"),
                                    user=_get_secret_data("user"),
                                    password=_get_secret_data("password")
                                )
    cursor = connection.cursor()
    return {"connection":connection, "cursor": cursor}

def _close_connection( connection:psycopg2.extensions.connection, cursor:psycopg2.extensions.cursor ):
    connection.close()
    cursor.close()

def get_score_table() -> dict:
    """
    Returns:
        dict: Score table
    """
    conn_data = _connect_to_database()
    connection = conn_data["connection"]
    cursor = conn_data["cursor"]
    
    cursor.execute("SELECT * FROM score ORDER BY tries ASC LIMIT 10;")
    score_table = cursor.fetchall()
    _close_connection( connection, cursor )
    return score_table


def add_score( new_name="none", final_score=-1 ) -> bool:
    if new_name=="none" or final_score==-1:return False
    if _user_exists_in_db( new_name ):
        if _is_db_score_lower( new_name, final_score ):return False
    
    conn_data = _connect_to_database()
    connection = conn_data["connection"]
    cursor = conn_data["cursor"]

    cursor.execute("""INSERT INTO score(\"name\", tries)
                   VALUES ('{0}', {1})
                   ON CONFLICT (\"name\")
                   DO UPDATE SET tries={1}""".format(new_name.lower(), final_score))
    connection.commit()
    
    _close_connection( connection, cursor )
    return True


def _user_exists_in_db( player_name:str ) -> bool:
    conn_data = _connect_to_database()
    connection = conn_data["connection"]
    cursor = conn_data["cursor"]
    
    cursor.execute("SELECT * FROM score WHERE \"name\"='{0}'".format( player_name.lower()))
    player_info = cursor.fetchone()

    _close_connection( connection, cursor )

    if player_info == None:
        return False
    return True

def _is_db_score_lower( player_name:str, new_score:int ) -> bool:
    conn_data = _connect_to_database()
    connection = conn_data["connection"]
    cursor = conn_data["cursor"]

    cursor.execute("SELECT * FROM score WHERE \"name\"='{0}'".format( player_name.lower()))
    player_info = cursor.fetchone()

    if player_info[2] <= new_score:
        return True
    
    return False