from connection import connect


def get_authors():
    conn = connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM author;"
    cursor.execute(sql)
    data = cursor.fetchall()
    conn.close()
    return data


if __name__ == '__main__':
    a = get_authors()
    print(a)
