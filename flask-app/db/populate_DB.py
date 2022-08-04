import sqlalchemy as db
import pandas as pd

engine = db.create_engine('mysql://root:@localhost/movie_emotions_map')
connection = engine.connect()
metadata = db.MetaData()

data=pd.read_csv('../static/new_csv/new_data_cluster_emotion.csv',header=0,index_col=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('moviesemotionmap', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_anger.csv',header=0,index_col=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2anger', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_anticipation.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2anticipation', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_disgust.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2disgust', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_fear.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2fear', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_joy.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2joy', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_sadness.csv',header=0,index_col=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2sadness', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_surprise.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2surprise', con=engine, if_exists='append', index=False)

#----------------------------------------------------------------------------------

data=pd.read_csv('../static/new_csv/lvl2_trust.csv',header=0)
data['plot']="nn"
data['poster']="nn"
data.to_sql('lvl2trust', con=engine, if_exists='append', index=False)

