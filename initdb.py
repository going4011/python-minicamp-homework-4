import sqlite3

connection = sqlite3.connect('database.db')
print('Opened Database successfully')

connection.execute('CREATE TABLE movies (movie_name TEXT, movie_year TEXT, movie_description TEXT)')
print ('Table created successfully')

connection.close()
