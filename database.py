import sqlite3
from sqlite3 import Error

sqlite_file = "trakt_shows.db"
table_name = "shows"

p_key_column = "p_key"
stub_column = "show_stub"
show_column = "show_name"
season_column = "season"
episode_number_column = "episode_number"
episode_title_column = "episode_title"
watched_status_column = "watched_status"
hidden_status_column = "hidden_status"

create_table_sql = f'CREATE TABLE {table_name} (' \
									 f'{p_key_column} TEXT PRIMARY KEY, ' \
									 f'{stub_column} TEXT, ' \
									 f'{show_column} TEXT, ' \
									 f'{season_column} INTEGER, ' \
									 f'{episode_number_column} INTEGER, ' \
									 f'{episode_title_column} TEXT, ' \
									 f'{watched_status_column} INTEGER, ' \
									 f'{hidden_status_column} INTEGER)'

def get_p_key(episode_info):
	""" create the primary key field by concatenating episode information
	:param episode_info: Dictionary of a single episode
	"""
	return f'{episode_info["show_stub"]}S{episode_info["season"]}E{episode_info["episode"]}'
	

def execute_sql(conn, query):
	""" execute a provided sql query on a provided connection
	:param conn: a database connection object
	:param query: a full sql query to execute
	"""
	try:
			c = conn.cursor()
			c.execute(query)
	except Error as e:
			print(f"SQL error :{e}")
			print(f"Attempted to run: {query}")
			
	return c

def create_connection(db_file):
	""" create a database connection to the SQLite database 
	:param db_file: the database file to connect to
	"""
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)
	
	return conn
	
		
def insert_row(conn, episode_info):
	""" inserts a row of episode data into the provided database connection
	:param conn: Connection object
	:param episode_info: dictionary of episode information
	"""
	p_key = get_p_key(episode_info)
	
	insert_statement = f'INSERT INTO shows (p_key, show_stub, show_name, season, episode_number, episode_title watched_status, hidden_status) VALUES (\"{p_key}\", \"{episode_info["show_stub"]}\", \"{episode_info["show_name"]}\", {episode_info["season"]}, {episode_info["episode_number"]}, {episode_info["episode_title"]}, {episode_info["watched_status"]}, {episode_info["hidden_status"]});'
	
	execute_sql(conn, insert_statement)
		

def update_status(conn, episode_info, status="watched_status"):
	""" update the watched status on a given row
	:param conn: Connection object
	:param episode_info: dictionary of episode information
	:param status: string, either "watched_status" or "hidden_status". Defaults to "watched_status"
	"""
	p_key = get_p_key(episode_info)
	
	status_update = f'UPDATE shows SET watched_status = {episode_info[status]} WHERE p_key = "{p_key}";'
	
	execute_sql(conn, status_update)
	
		
def get_latest_unwatched(conn, show_stub):
		""" pull the latest episode of a given show that is available to watch and currently unwatched
		:param show_stub: trak.tv stub of the show to search for
		"""
		sql_query = f'SELECT "show_name", "season", "episode_number", "episode_title" FROM shows WHERE show_stub = "{show_stub}" AND "watched_status" = 0 ORDER BY "season", "episode"'
		
		episode_list = execute_sql(conn, sql_query).fetchall()
		
		return episode_list
		

if __name__ == "__main__":
	conn = create_connection(sqlite_file)
	
	print(get_latest_unwatched(conn, 'game-of-thrones'))
	
	conn.commit()
	conn.close()