import sqlite3
from faker import Faker

conn = sqlite3.connect("Movies.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

data = cursor.execute("SELECT genres FROM movies").fetchall()
genres_set = set()
for row in data:
    if row['genres'] is None:
        continue
    movie_genres = row['genres'].split('|')
    # Надо добавлять во множество не списки жанров для каждого фильма, а сами жанры из этого списка
    # Для этого используем функцию update
    genres_set.update(movie_genres)
genres = sorted(list(genres_set))
genres = [(genre, ) for genre in genres]
cursor.executemany("INSERT INTO genres (name) VALUES(?);", genres)
conn.commit()
