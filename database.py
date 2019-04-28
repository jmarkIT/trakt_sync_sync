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
									 f'{season_column} INTEGER, ' \
									 f'{episode_column} INTEGER, ' \
									 f'{watched_status_column} INTEGER, ' \
									 f'{hidden_status_column} INTEGER)'


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
		
		
def insert_row(conn, episode_info):
	p_key = f'{episode_info["show_stub"]}S{episode_info["season"]}E{episode_info["episode"]}'
	
	insert_statement = f'INSERT INTO shows (p_key, show_stub, show_name, season, episode, watched_status, hidden_status) VALUES (\"{p_key}\", \"{episode_info["show_stub"]}\", \"{episode_info["show_name"]}\", {episode_info["season"]}, {episode_info["episode"]}, {episode_info["watched_status"]}, {episode_info["hidden_status"]});'
	
	try:
		c = conn.cursor()
		c.execute(insert_statement)
	except Error as e:
		print(e)
		
	

if __name__ == "__main__":
	conn = create_connection(sqlite_file)
	
	create_table(conn, create_table_sql)
	
	episode_info = { "show_stub": "game-of-thrones", "show_name" : "Game of Thrones", "season" : 1, "episode" : 1, "watched_status" : 1, "hidden_status" : 0 }
	
	insert_row(conn, episode_info)
	
	conn.commit()
	conn.close()