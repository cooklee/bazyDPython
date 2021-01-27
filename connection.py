import psycopg2

data = {
    'user': 'postgres',
    'password': 'vetjopoco',
    'host': "localhost",
    'dbname': 'przyklad'
}
connection = psycopg2.connect(**data)  # psycopg2.connect(USER='postgres', PASSWORD='vetjopoco'...)
connection.autocommit = True
cursor = connection.cursor()
insert_query = "insert into products (name,price) values ('Słonina', 3.67);"
cursor.execute(insert_query)

query = """
SELECT * FROM products;
"""
cursor.execute(query)
for row in cursor:
    print(row)





connection.close()
