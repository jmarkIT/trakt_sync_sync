import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	""" create a database connection to the SQLite database """
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
	except Error as e:
		print(e)
	
	return None
	

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