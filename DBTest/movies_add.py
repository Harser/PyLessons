import sqlite3



conn = sqlite3.connect("Movies.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

genres = cursor.execute("SELECT * FROM genres").fetchall()
genres = {genre['name']: genre['id'] for genre in genres}
print(genres)
movie_genre_list = []
movies = cursor.execute("SELECT id, genres FROM movies").fetchall()
for movie in movies:
    if not movie['genres']:
        continue
    for genre in movie['genres'].split('|'):
        genre_id = genres[genre]
        movie_genre_list.append((movie['id'], genre_id))
cursor.executemany("INSERT INTO movies_genres_through(movies_id, genres_id) VALUES(?, ?);", movie_genre_list)

conn.commit()
