from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route('/addmovie', methods = {'POST'})
def addmovie():
    connection=sqlite3.connect('database.db')
    cursor = connection.cursor()
    print ('connection opened')

    try:
        movie_name = request.form['movie_name']
        movie_year = request.form['movie_year']
        movie_description = request.form['movie_description']
        print('values added')
        cursor.execute('INSERT INTO movies (movie_name, movie_year, movie_description) VALUES (?, ?, ?)', (movie_name, movie_year, movie_description))
        print('values inserted into database')
        connection.commit()
        print('values finalized')
        message = 'Record Successfully Added'

    except:
        connection.rollback()
        message = 'Error in Insert Operation'

    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/movielist')
def movielist():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movieList = cursor.fetchall()
    connection.close()
    return jsonify(movieList)
