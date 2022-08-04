from distutils.log import debug
from distutils.util import execute
from itertools import count
import json
from operator import truediv
from telnetlib import IP

from flask import make_response,Flask, send_from_directory, request, render_template, jsonify, redirect, url_for
import sys
import mysql.connector
import db.mongo_functions as mf
import sqlalchemy as db
import pandas as pd
# import gevent.pywsgi
# import socket

engine = db.create_engine('mysql://root:@localhost/movie_emotions_map')


app = Flask(__name__)






def load_data():

    
    sql_statement = "SELECT * FROM MoviesEmotionMap"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/new_data_cluster_emotion.csv")


    sql_statement = "SELECT * FROM lvl2anger"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_anger.csv")

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2anticipation"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_anticipation.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2disgust"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_disgust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2fear"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_fear.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2joy"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_joy.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2sadness"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_sadness.csv")

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2surprise"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_surprise.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    sql_statement = "SELECT * FROM lvl2trust"
    df = pd.read_sql(sql_statement, con=engine)
    df.to_csv("static/new_csv/lvl2_trust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------

# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def get_index():
    # getting the index.html (homepage)
    return render_template('index.html')

 
def load_dataJS(data):

    id_tuple = tuple(data)

    print("*********************************************************")
    query= 'SELECT * FROM MoviesEmotionMap WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/new_data_cluster_emotion.csv")


    
    query= 'SELECT * FROM lvl2anger WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_anger.csv")

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2anticipation WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_anticipation.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2disgust WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_disgust.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2fear WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_fear.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2joy WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_joy.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2sadness WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_sadness.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2surprise WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_surprise.csv", index=False)

    # -----------------------------------------------------------------------------------------------------
    query= 'SELECT * FROM lvl2trust WHERE _id IN {};'.format(id_tuple)
    df = pd.read_sql(query, con=engine)
    df.to_csv("static/new_csv/lvl2_trust.csv", index=False)

    
    # -----------------------------------------------------------------------------------------------------



@app.route('/', methods=['GET', 'POST'])
def getJS_postMongoDB():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    
    if request.method == "POST":
        title = request.json['title']
        director = request.json['director']
        star = request.json['star']
        word = request.json['word']
        genre = request.json['genre']
        numberofmap = request.json['numberofmap']
        
        if title != '':
            load_dataJS(mf.getMoviesByTitle(title))
        if  director !='':
            print(mf.getMoviesForDirector(director))
            load_dataJS(mf.getMoviesForDirector(director))
        if star != '':
            load_dataJS(mf.getMoviesForStar(star))
        if  word != '':
            load_dataJS(mf.getMoviesIdByStringInReview(word))
        if  genre != '':
            print(mf.getMoviesByGenre(genre))
            load_dataJS(mf.getMoviesByGenre(genre))
        
        if numberofmap == -1:  
            load_data()
        
        app.config["TEMPLATES_AUTO_RELOAD"] =True
        
        return render_template('index.html')

    return render_template('index.html')


# ********   Main    ********
if __name__ == '__main__':
    # specify an ip address to make flask run on it
    ip="35.223.110.133"
    # specify the port that the web server is listening on
    port='80'

    load_data()
   
    app.run(host='0.0.0.0')
    