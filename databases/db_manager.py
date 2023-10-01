import psycopg2
import json



def _get_secret_data( name="", secret_file="databases/secret_keys.json" ) -> dict:
    with open( secret_file, "r" ) as file:
        data = json.load(file)
        return data[name]
        
def _connect_to_database( file_path="databases/secret_keys.json" ):
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
    cursor.close()
    connection.close()
    return score_table

def add_score( new_name="none", final_score=-1 ) -> bool:
    if new_name=="none" or final_score==-1:return
    
    conn_data = _connect_to_database()
    connection = conn_data["connection"]
    cursor = conn_data["cursor"]

    cursor.execute("INSERT INTO score(\"name\", tries) VALUES ('{0}', {1})".format(new_name, final_score))
    connection.commit()
    
    cursor.close()
    connection.close()
    return True