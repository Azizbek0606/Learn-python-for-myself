import psycopg2

conn = psycopg2.connect(
    "dbname='example' user='postgres' host='localhost' password='Azizbek.5474' port='5432'"
)
cur = conn.cursor()
# cur.execute(
#     """
# select * from employee
# where first_name = 'azizbek'
# """
# )

# records = cur.fetchall()
# conn.close()
# print(records)


insert_sql = (
    "INSERT INTO employee (first_name,last_name , email , gender , date_of_birth , country_of_birth, position)"
    "VALUES (%s,%s,%s,%s,%s,%s,%s)"
)
cur.execute(insert_sql, (
    "example" , "last_example_name" , "example@gmail.com" , "male" , "2010-10-10" , "uzbekistan" , "student"
))
conn.commit()
cur.close()
conn.close()