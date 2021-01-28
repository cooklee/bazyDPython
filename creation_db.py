from connection import connect
from create_query_sql import creation_query_list

def create_db(query_list=None):
    if query_list is None:
        query_list = creation_query_list
    conn = connect()
    cursor = conn.cursor()
    for query in query_list:
        try:
            cursor.execute(query)
        except:
            table  =query.split('\n')[1][:-1]
            print(f"nie udało sie wykonać zapytania {table}")
    conn.close()

if __name__ == "__main__":
    create_db()



