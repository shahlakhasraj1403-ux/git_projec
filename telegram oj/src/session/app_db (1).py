import sqlite3

DB_NAME = 'MoviesApiInfo.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.close()

# init_db()

def create_table(DB_NAME, table_name = 'MoviesData'):
    query = f''' CREATE TABLE IF NOT EXISTS {table_name}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        year INTEGER,
        imdb_rate REAL,
        genres TEXT,
        poster TEXT
        )
        '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

# create_table(DB_NAME, 'MoviesData')
def insert_record(title, year, imdb_rate, genres, poster):
    query = f'''INSERT INTO MoviesData (title, year, imdb_rate, genres, poster)
    VALUES(?, ?, ?, ?, ?)
    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, year, imdb_rate, genres, poster))
    conn.commit()
    conn.close()

##############################################
# insert_record('Inception', 2001, 7.8, 'Action , Drama', 'http://test.com')


def insert_list_of_movies(movies_list):
    
    for item in movies_list:
        print(item)
        title = item['title']
        year = item['year']
        imdb_rate = item['imdb_rating']
        genres = ','.join(item ['genres'])
        poster = item['poster']
        insert_record(title, year, imdb_rate, genres, poster)

    return f'{len(movies_list)} Record Inserted Successfully'

#########################################################
# movie_list = [{'title':'God Father', 'year': 2020, 'imdb_rate':8.5, 
#                'genres':'Action , Drama', 'poster':'http://test1.com'},
#                {'title':'Dark Night', 'year': 2004, 'imdb_rate':6.3, 
#                'genres':'Action , Mystry', 'poster':'http://test2.com'}]
# print(insert_list_of_movies(movie_list))

#########################################################
# جدول و متدهای مربوط به فیلم‌های یک ژانر خاص (title, poster, genres)
#########################################################

def create_genre_movies_table(DB_NAME, table_name='GenreMoviesData'):
    query = f''' CREATE TABLE IF NOT EXISTS {table_name}
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genres TEXT,
        poster TEXT
        )
        '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

# create_genre_movies_table(DB_NAME)


def insert_genre_movie_record(title, genres, poster):
    query = f'''INSERT INTO GenreMoviesData (title, genres, poster)
    VALUES(?, ?, ?)
    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, genres, poster))
    conn.commit()
    conn.close()


def insert_list_of_genre_movies(movies_list):

    for item in movies_list:
        title = item['title']
        genres = ','.join(item['genres'])
        poster = item['poster']
        insert_genre_movie_record(title, genres, poster)

    return f'{len(movies_list)} Record Inserted Successfully'