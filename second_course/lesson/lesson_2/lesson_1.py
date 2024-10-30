import psycopg2

conn = psycopg2.connect("dbname='example' user='postgres' host='localhost' password='Azizbek.5474' port='5432'")
cur = conn.cursor()
cur.execute(
    """
update employee set first_name = 'azizbek', last_name = 'xabibullayev', email='ax@gmail.com'
where last_name = 'Matchitt'
"""
)

records = cur.fetchall()
print(records)
