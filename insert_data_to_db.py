from connection import connect

def dodaj_autora(first_name, last_name):
    sql = f"""
    INSERT INTO author (first_name, last_name) values 
                       ('{first_name}', '{last_name}');
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()

def dodaj_ksiazke(title, id_author):
    sql = f"""
        INSERT INTO book (title, id_author) values 
                           ('{title}', {id_author});
        """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.close()
