import os
from bson import ObjectId
from tqdm import tqdm
import pandas as pd
import csv
import numpy as np
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pymongo import MongoClient
import certifi
ca = certifi.where()


client =MongoClient("localhost", 27017)
db_reviews = client["EmotionDB"]
MOVIES_REVIEWS = "Movies"
MOVIES_DETAILS = "MovieDetails"

CONNECTION_STRING = 'mongodb+srv://liorlansman:lior1989@emotionsinmovies.sykue.mongodb.net/emotionsdbnew?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING)
db = client["emotionsdbnew"]
MOVIES = "moviesfinalcollection"


def get_percentiles():
    """ get all glyphes from the db"""

    movies = db[MOVIES].find({}, {"_id": 0, "titleId": 1, "signature_percentile": 1})
    ls_data = []
    for movie in movies:
        data = movie.pop("signature_percentile")
        data["titleId"] = movie['titleId']
        ls_data.append(data)

    df = pd.DataFrame(ls_data)
    return df

def strStemmingAndCaseFolding(str):
    ps = PorterStemmer()
    words = word_tokenize(str)
    stemming_list=''
    for w in words:
        stemming_list+= ' ' + ps.stem(w).casefold()
    return stemming_list
def getNameByMovieId(movieid):
    try:
        query = db_reviews[MOVIES_REVIEWS].find({"details_id": movieid})
        for result in query:
            try:
                return result['reviews_num'],result['additional_data']['movie_id']
            except:
                return result['reviews_num'],None
    except:
        return None,None


def getMovieGenre(movieid):
    query = db[MOVIES].find({"details_id": movieid}, {"_id": 0})
    for result in query:
        if movieid.__str__() == result['details_id'].__str__() :
            return result['additional_data']['movie_genres']

def isMovieHasThisGenre(movieid,genre):
    try:
        return str(genre).lower().strip() in getMovieGenre(movieid).lower().strip()
    except:
        # Not all the data has genre , due to messing data in my pc
        return False


def isMovieHaveEmotion(Movie_id,emotion):
    percentiles=get_percentiles()
    movie_index = percentiles[percentiles["titleId"] == Movie_id].index.values[0]
    data = percentiles.drop("titleId", axis=1)
    percentile_value=data.at[movie_index,emotion]
    print(percentile_value)
    if float(percentile_value) > 50 :
        return True
    return False

def getMoviesIdByStringInReview(str):
    '''
           Input : string or sentence
           Output : return all the movies ids that at least 10% of their reviews contain the str

           example : getMoviesByGenre('Drama')
    '''
    movies_list=[]
    if str != None and str.split(' ').__len__()==1:
        str = strStemmingAndCaseFolding(str)

    query = db_reviews[MOVIES_DETAILS].find()

    for result in query:
        count =0
        for r in result['reviews']:
            reviews_text=r['text']
            if str.split(' ').__len__() == 1:
                reviews_text = strStemmingAndCaseFolding(r['text'])
            if str in reviews_text:
                count+=1
        reviews_num,movie_id = getNameByMovieId(movieid=result['_id'])
        if movie_id!=None and float(count) >= float((10 * reviews_num) / 100):
            movies_list += [movie_id]
    return movies_list

def getMoviesByGenre(genre):
    '''
           Input : genre type (one genre)
           Output : return all the movies ids that has the genre type

           example : getMoviesByGenre('Drama')
    '''
    genre = genre.lower().title()
    query = db[MOVIES].find({'movie_genres': {'$regex': str(genre)}})
    Movies_List = []
    for result in query:
        Movies_List += [str(result['_id'])]
    return Movies_List
def getMoviesForStar(star_name):
    '''
        Input : star name
        Output : return all the movies ids that the star participate in it.

        example : getMoviesForStar('carla Gugino')
    '''
    star_name=star_name.lower().title()
    query = db[MOVIES].find({'movie_stars':{'$regex':str(star_name)}})
    Movies_List =[]
    for result in query:
        Movies_List += [str(result['_id'])]
    return Movies_List

def getMoviesForDirector(Director_name):
    '''
        Input : director name
        Output : return all the movies ids that the director participate in it.

        example : getMoviesForDirector('Mike Flanagan')
    '''
    Director_name=Director_name.lower().title()
    query = db[MOVIES].find({'movie_directors':{'$regex':str(Director_name)}})
    Movies_List =[]
    for result in query:
        Movies_List += [str(result['_id'])]
    return Movies_List


def getMoviesByTitle(title):
    '''
    Input : movie name
    Output : return all the movies ids with the title

    example : getMoviesByTitle('the kid'))
    '''
    title=title.lower().title()
    query = db[MOVIES].find({'name':{'$regex':str(title)}})
    Movies_List =[]
    for result in query:
        Movies_List += [str(result['_id'])]
    return Movies_List
