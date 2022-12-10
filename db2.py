import sqlite3

conn = sqlite3.connect("users.sqlite")

cursor = conn.cursor()

sql_query = """CREATE TABLE users (
id integer PRIMARY KEY,
first_name NUT NULL
last_name NUT NULL
p_number NUT NULL
location NUT NULL
gender NUT NULL
rel_status NUT NULL
intersted_in NUT NULL
hobbis NUT NULL
friends NUT NULL
)"""

cursor.execute(sql_query)
