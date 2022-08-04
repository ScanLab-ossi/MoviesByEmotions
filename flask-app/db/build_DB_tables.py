import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="Movie_Emotions_Map")
cursor = connection.cursor()
# Query for creating table
drop_a="DROP TABLE IF EXISTS lvl2anger"
drop_j="DROP TABLE IF EXISTS lvl2joy"
drop_s="DROP TABLE IF EXISTS lvl2sadness"
drop_su="DROP TABLE IF EXISTS lvl2surprise"
drop_f="DROP TABLE IF EXISTS lvl2fear"
drop_an="DROP TABLE IF EXISTS lvl2anticipation"
drop_t="DROP TABLE IF EXISTS lvl2trust"
drop_d="DROP TABLE IF EXISTS lvl2disgust"
drop_m="DROP TABLE IF EXISTS MoviesEmotionMap"
cursor.execute(drop_m)

cursor.execute(drop_d)
cursor.execute(drop_a)

cursor.execute(drop_j)

cursor.execute(drop_s)

cursor.execute(drop_su)

cursor.execute(drop_f)

cursor.execute(drop_an)

cursor.execute(drop_t)

cursor.execute(drop_s)



sql_statement_moviesemotionmap="CREATE TABLE `MoviesEmotionMap` (`_id` varchar(255),`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` varchar(255) NOT NULL,`poster` varchar(255) NOT NULL,`release_year`varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"

sql_statement_lvl2anger="CREATE TABLE `lvl2anger`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255),`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2joy=	"CREATE TABLE `lvl2joy`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2sadness=	"CREATE TABLE `lvl2sadness`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2surprise=	"CREATE TABLE `lvl2surprise`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2fear=	"CREATE TABLE `lvl2fear`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2anticipation=	"CREATE TABLE `lvl2anticipation`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2trust=	"CREATE TABLE `lvl2trust`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255) ,`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
sql_statement_lvl2disgust=	"CREATE TABLE `lvl2disgust`(`_id` varchar(255) NOT NULL,`movie_directors` text ,`movie_genres` varchar(255) NOT NULL,`movie_rating` float NOT NULL,`movie_stars` varchar(255),`movie_writers` varchar(255) ,`name` varchar(255) NOT NULL,`plot` text NOT NULL,`poster` text NOT NULL,`release_year` varchar(4) NOT NULL,`reviews_num` int(11) NOT NULL,`titleId` varchar(255) NOT NULL,`tsne_glyph_x` float(15) NOT NULL,`tsne_glyph_y` float(15) NOT NULL,`signature_zscore_percent_anger` float(15) NOT NULL,`signature_zscore_percent_anticipation` float(15) NOT NULL,`signature_zscore_percent_disgust` float(15) NOT NULL,`signature_zscore_percent_fear` float(15) NOT NULL,`signature_zscore_percent_joy` float(15) NOT NULL,`signature_zscore_percent_sadness` float(15) NOT NULL,`signature_zscore_percent_surprise` float(15) NOT NULL,`signature_zscore_percent_trust` float(15) NOT NULL,`cluster_1` int(11) NOT NULL,`emotion_color` int(11) NOT NULL,`cluster_level2` int(11) NOT NULL,`tsne_glyph_x_level2` float(15) NOT NULL,`tsne_glyph_y_level2` float(15) NOT NULL,`emotion_color_lvl2` int(11) NOT NULL,PRIMARY KEY(_id)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"


cursor.execute(sql_statement_moviesemotionmap)
cursor.execute(sql_statement_lvl2anger)
cursor.execute(sql_statement_lvl2joy)
cursor.execute(sql_statement_lvl2sadness)
cursor.execute(sql_statement_lvl2surprise)
cursor.execute(sql_statement_lvl2fear)
cursor.execute(sql_statement_lvl2anticipation)
cursor.execute(sql_statement_lvl2trust)
cursor.execute(sql_statement_lvl2disgust)

connection.close()
