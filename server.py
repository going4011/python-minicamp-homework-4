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
    return render_template('home.html')
