from utilities import get_db,do_query

connection = get_db()

# REQUIREMENTS:

# Production Company Details:

# budget per year
def budget_per_year():
	query = "SELECT pc.company_name, YEAR(m.release_date) as year, SUM(m.budget) as total_budget FROM d_production_company pc",
	"LEFT OUTER JOIN f_movie_production mp ON pc.id = mp.production_company_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mp.movie_id",
	"GROUP BY pc.company_name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), SUM(m.budget);"

	query_response = do_query(connection,movie_query)

	return query_response

# revenue per year
def revenue_per_year():
	query = "SELECT pc.company_name, YEAR(m.release_date) as year, SUM(m.revenue) as total_revenue FROM d_production_company pc",
	"LEFT OUTER JOIN f_movie_production mp ON pc.id = mp.production_company_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mp.movie_id",
	"GROUP BY pc.company_name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), SUM(m.revenue);"

	query_response = do_query(connection,movie_query)

	return query_response

# profit per year
def profit_per_year():
	query = "SELECT pc.company_name, YEAR(m.release_date) as year, (SUM(m.revenue)-SUM(m.budget)) as total_profit FROM d_production_company pc",
	"LEFT OUTER JOIN f_movie_production mp ON pc.id = mp.production_company_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mp.movie_id",
	"GROUP BY pc.company_name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), (SUM(m.revenue)-SUM(m.budget));"

	query_response = do_query(connection,movie_query)

	return query_response

# releases by genre per year
def releases_by_genre_per_year():
	query = "SELECT pc.company_name, g.name as genre_name, YEAR(m.release_date) as year, COUNT(m.id) as genre_count FROM d_production_company pc",
	"LEFT OUTER JOIN f_movie_production mp ON pc.id = mp.production_company_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mp.movie_id",
	"LEFT OUTER JOIN f_movie_genre mg ON m.id = mg.movie_id",
	"LEFT OUTER JOIN d_genre g ON g.id = mg.genre_id",
	"GROUP BY pc.company_name, YEAR(m.release_date), g.name",
	"ORDER BY pc.company_name, g.name, YEAR(m.release_date), COUNT(m.id);"

	query_response = do_query(connection,movie_query)

	return query_response

# average popularity of produced movies per year
def avg_popularity_per_year():
	query = "SELECT pc.company_name, YEAR(m.release_date) as year, AVG(mr.rating) as avg_rating FROM d_production_company pc",
	"LEFT OUTER JOIN f_movie_production mp ON pc.id = mp.production_company_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mp.movie_id",
	"LEFT OUTER JOIN f_movie_rating mr ON m.id = mr.movie_id",
	"GROUP BY pc.company_name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), AVG(mr.rating);"

	query_response = do_query(connection,movie_query)

	return query_response

# Movie Genre Details:

# most popular genre by year
def releases_by_genre_per_year():
	query = "SELECT g.name as genre_name, YEAR(m.release_date), AVG(mr.rating) as avg_rating FROM d_genre g",
	"LEFT OUTER JOIN f_movie_genre mg ON g.id = mg.genre_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mg.movie_id",
	"LEFT OUTER JOIN f_movie_rating mr ON m.id = mr.movie_id",
	"GROUP BY g.name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), AVG(mr.rating);"

	query_response = do_query(connection,movie_query)

	return query_response

# budget by genre by year
def releases_by_genre_per_year():
	query = "SELECT g.name as genre_name, YEAR(m.release_date), SUM(m.budget) as budget FROM d_genre g",
	"LEFT OUTER JOIN f_movie_genre mg ON g.id = mg.genre_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mg.movie_id",
	"GROUP BY g.name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), SUM(m.budget);"

	query_response = do_query(connection,movie_query)

	return query_response


# revenue by genre by year
def releases_by_genre_per_year():
	query = "SELECT g.name as genre_name, YEAR(m.release_date), SUM(m.revenue) as revenue FROM d_genre g",
	"LEFT OUTER JOIN f_movie_genre mg ON g.id = mg.genre_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mg.movie_id",
	"LEFT OUTER JOIN f_movie_rating mr ON m.id = mr.movie_id",
	"GROUP BY g.name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), SUM(m.budget);"

	query_response = do_query(connection,movie_query)

	return query_response


# profit by genre by year
def releases_by_genre_per_year():
	query = "SELECT g.name as genre_name, YEAR(m.release_date), (SUM(m.revenue)-SUM(m.budget)) as profit FROM d_genre g",
	"LEFT OUTER JOIN f_movie_genre mg ON g.id = mg.genre_id",
	"LEFT OUTER JOIN d_movie m ON m.id = mg.movie_id",
	"LEFT OUTER JOIN f_movie_rating mr ON m.id = mr.movie_id",
	"GROUP BY g.name, YEAR(m.release_date)",
	"ORDER BY pc.company_name, YEAR(m.release_date), (SUM(m.revenue)-SUM(m.budget));"

	query_response = do_query(connection,movie_query)

	return query_response


#Could make other requests such as the ones below
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
