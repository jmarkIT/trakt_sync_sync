import sqlite3
from sqlite3 import Error

sqlite_file = "trakt_shows.sqlite"
table_name = "shows"
id_column = "show_name"
field_type = "TEXT"


def create_connection(db_file):
	""" create a database connection to the SQLite database """
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)
	
	return conn
	

def create_table(conn, create_table_sql):
	""" create a table from the create_table_sql statement
	:param conn: Conection Object
	:param create_table_sql: a CREATE TABLE statement
	:return:
	"""
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)
		
		
if __name__ == "__main__":
	create_table_sql = f'CREATE TABLE {table_name} ({id_column} {field_type} PRIMARY KEY)'
	
	conn = create_connection(sqlite_file)
	
	create_table(conn, create_table_sql) 

