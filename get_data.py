from connection import connect


def get_authors():
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM author;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

def get_books():
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM book;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data

def get_book_by_id(id):
    conn = connect()
    cursor = conn.cursor()
    sql = f"SELECT * FROM book where id={id};"
    cursor.execute(sql)
    data = cursor.fetchone()
    conn.close()
    return data


if __name__ == '__main__':
    a = get_authors()
    print(a)
