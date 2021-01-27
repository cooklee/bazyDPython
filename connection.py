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

query = """
SELECT * FROM products;
"""
cursor.execute(query)
for row in cursor:
    print(row)





connection.close()
