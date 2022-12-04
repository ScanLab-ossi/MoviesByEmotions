import csv
import os
import time

from tqdm import tqdm
from pymongo import MongoClient
import json
import glob
import certifi
ca = certifi.where()

from UpdateMongoDB.backend import NRC_Processor
from UpdateMongoDB.config.config_functions import load_config
from UpdateMongoDB.definitions import DATA_DIR

MOVIES = "Movies"
MOVIES_DETAILS = "MovieDetails"


# TODO refactor this class
class MongoDB:
    def __init__(self, ip="localhost", port=27017, data_dir=DATA_DIR, fill=False):
        self._ip = ip
        self._port = port
        self._db = None
        self._data_dir = data_dir
        self._fill = fill

    @property
    def db(self):
        if self._db is None:
            self._setup_db()
        return self._db

    def _connect_db(self):
        """ connects to db  """
        client =MongoClient(self._ip, self._port)
        self._db = client["EmotionDB"]

    def _fill_db(self):
        """ fill database with data from given dir path"""
        MongoClient(self._ip, self._port).drop_database('EmotionDB')
        self._connect_db()

        jsons = glob.glob(os.path.join(self._data_dir, "*.json"))
        for js in tqdm(jsons):
            js = os.path.join(self._data_dir, js)

            if js.endswith('.json'):
                with open(js, encoding="utf8") as file:
                    js_dict = json.load(file)

                    # create document for movie
                    signature = NRC_Processor.process_movie(js_dict)

                    # insert reviews
                    movie_details_insert = {
                        "reviews": js_dict["reviews"],
                        "signature": signature
                    }
                    result = self._db["MovieDetails"].insert_one(movie_details_insert)
                    movie_insert = {
                        "titleId": js_dict["titleId"],
                        "name": js_dict["name"],
                        "details_id": result.inserted_id,
                        "reviews_num": len(js_dict["reviews"]),
                        "additional_data": {}

                    }

                    result = self._db["Movies"].insert_one(movie_insert)
        print(os.path.join(self._data_dir, "Copy of finalCollection.csv"))
        additional_data = os.path.join(self._data_dir, "Copy of finalCollection.csv")
        with open(additional_data, newline='', encoding='latin1') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            header = next(spamreader)
            line_movie_id=header.index('_id')
            line_movie_rating=header.index('movie_rating')
            line_movie_directors=header.index('movie_directors')
            line_movie_writers=header.index('movie_writers')
            line_movie_stars=header.index('movie_stars')
            line_movie_genres=header.index('movie_genres')
            line_release_year=header.index('release_year')
            line_titleId=header.index('titleId')

            for row in spamreader:
                titleId = 'tt0' + row[line_titleId][2:]
                # print(titleId)
                dc = {
                    "movie_id": row[line_movie_id],
                    "movie_rating": row[line_movie_rating],
                    "movie_directors": row[line_movie_directors],
                    "movie_writers": row[line_movie_writers],
                    "movie_stars": row[line_movie_stars],
                    "movie_genres": row[line_movie_genres],
                    "release_year": row[line_release_year]
                }
                self._db[MOVIES].update_one({"titleId": titleId}, {"$set": {"additional_data": dc}})

    def _setup_db(self):
        self._connect_db()
        if self._fill:
            start = time.time()
            self._fill_db()
            print(time.time() - start)


config = load_config("backend_config")
db = MongoDB(port=config["port"],ip=config["ip"],fill=config["fill"]).db
