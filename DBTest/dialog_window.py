import sqlite3

conn = sqlite3.connect("Movies.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

movie_name = '%' + input() + '%'
movies_arr = cursor.execute("SELECT * FROM v_movies WHERE title like ?", (movie_name,)).fetchall()

def print_movie_info(movie):
    print('Название:', movie['title'])
    print('Год выпуска:', movie['year'])
    print('Жанры:',movie['genres'])
    print('Количество оценок:', movie['viewCount'])
    print('Средняя оценка:', movie['averageRating'])

if len(movies_arr) == 0:
    print('Такого фильма нет в нашем рейтинге.')
elif len(movies_arr) == 1:
    print('Единственное совпадение в нашем рейтинге:')
    print_movie_info(movies_arr[0])
else:
    print('Все совпадения по вашему запросу:')
    for movie in movies_arr:
        print_movie_info(movie)
        print()

conn = sqlite3.connect("Movies.db")
cursor = conn.cursor()

rec1 = input().split()
rec2 = input().split()
rec3 = input().split()
update_ratings = [rec1, rec2, rec3]
cursor.executemany("INSERT INTO ratings (userId, movieId, rating) VALUES(?, ?, ?);", update_ratings)

conn.commit()