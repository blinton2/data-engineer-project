from utilities import get_db,do_query

connection = get_db()

#Movies api function with optional argument for movie id
def movies(movie_id=-1):
	if movie_id != -1:
		movie_query = "SELECT * FROM d_movie where id = 1;"
		
	else:
		movie_query = "SELECT * FROM d_movie;"

	movie_response = do_query(connection,movie_query)

	return movie_response

def crews(crew_id=-1):
	print("Retrieve crew table")

def movie_ratings(movie_id=-1):
	print("Retrieve movie ratings")
