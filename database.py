import sqlite3
from sqlite3 import Error

sqlite_file = "trakt_shows.db"
table_name = "shows"

p_key_column = "p_key"
stub_column = "show_stub"
show_column = "show_name"
season_column = "season"
episode_column = "episode"
watched_status_column = "watched_status"
hidden_status_column = "hidden_status"

create_table_sql = f'CREATE TABLE {table_name} (' \
									 f'{p_key_column} TEXT PRIMARY KEY, ' \
									 f'{stub_column} TEXT, ' \
									 f'{show_column} TEXT, ' \
									 f'{season_column} TEXT, ' \
									 f'{episode_column} TEXT, ' \
									 f'{watched_status_column} TEXT, ' \
									 f'{hidden_status_column} TEXT)'


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
		
		
def insert_row(conn, show_stub, show_name, season, episode, watched_status, hidden_status):
	p_key = f"{show_stub}s{season}e{episode}"
	
	insert_statement = f"INSERT INTO show (p_key, show_stub, show_name, season, episode, watched_status, hidden_status) VALUES ({p_key}, {show_stub}, {show_name}, {season}, {episode}, {watched_status}, {hidden_status})"
	
	try:
		c = conn.cursor()
		c.execute(insert_statement)
	except Error as e:
		print(e)
		
	

if __name__ == "__main__":
	conn = create_connection(sqlite_file)
	
	create_table(conn, create_table_sql) 