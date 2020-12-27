#libraries
import numpy as np
import pandas as pd
from network import *
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras import layers
from archive.datasetloader import load_data
from archive.datapreprocessor import datapreprocessor
from archive.database_functions import rate,authenticate
from flask import Flask , render_template, request,redirect

# Number of users is 943


EMBEDDING_SIZE = 50

lens, user_id, num_movies, num_users, xtrain, ytrain, xval, yval , movie_id ,id_movie , user_id , id_user  = datapreprocessor()

movies = lens['title'].unique()

lens = rate(1 , "Sliding Doors (1998)" , 5 , lens , movies)
logins = [[i+1,i+1] for i in range(943)]
logins = pd.DataFrame(logins , columns = ['user_id','password'])




model = RecommenderNet(num_users, num_movies, EMBEDDING_SIZE)
model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(), optimizer=keras.optimizers.Adam(lr=0.001)
)

history = model.fit(
    x=xtrain,
    y=ytrain,
    batch_size=64,
    epochs=5,
    verbose=1,
    validation_data=(xval, yval),
)



model = RecommenderNet(num_users, num_movies, EMBEDDING_SIZE)
model.compile(
    keras.optimizers.Adam(lr=0.001), loss="mean_squared_error",
    metrics=["mean_absolute_error", "mean_squared_error"])

app = Flask(__name__)

@app.route('/ratings',methods = ['POST','GET'])
def route():
    movies = list(lens['title'].unique())
    return render_template('ratings.html',movie = movies)

@app.route('/sendrating', methods = ['POST','GET'])
def sendrating():
    if request.method == 'POST':
        result = request.form
        print(result)
    return redirect('/')

@app.route('/loginsend', methods = ['POST','GET'])
def loginsend():
    if request.method == 'POST':
        result = request.form
        print(result)
    return redirect('/movies')

@app.route('/error', methods = ['POST','GET'])
def error():
    data = "Agreed"
    return render_template('error.html',data=data)



@app.route('/' , methods = ['POST','GET'])
def display():
    return render_template('index.html')

@app.route('/login')
def login():   
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/send',methods = ['POST', 'GET'])
def send():
    if request.method == 'POST':
        result = request.form
        print(result)


    return redirect('/login')

    
@app.route('/movies')
def index():        
    user_selected = lens.user_id.sample(3).iloc[2]

    movies_watched_by_user = lens[lens.user_id == 1000]

    print(movies_watched_by_user)

    movies_not_watched = lens[~lens["movie_id"].isin(movies_watched_by_user.movie_id.values)
    ]["movie_id"]

    movies_not_watched = list(
        set(movies_not_watched).intersection(set(movie_id.keys()))
    )

    movies_not_watched = [[movie_id.get(x)] for x in movies_not_watched]

    user_encoder = user_id.get(user_selected)

    user_movie_array = np.hstack(
        ([[user_encoder]] * len(movies_not_watched), movies_not_watched)
    )  #user_movie_array consists of selected_user in userfind and moviefind

    rate = model.predict(user_movie_array)
    ratings = model.predict(user_movie_array).flatten()

    #For any iterable in python [-10:] denotes the indexing of last 10 items of that iterable.
    #[::-1] denotes same list in reverse order
    #returns top 10 max ratings' indices
    top_ratings_indices = ratings.argsort()[-10:][::-1]
    recommended_movie_ids = [
        id_movie.get(movies_not_watched[x][0]) for x in top_ratings_indices
    ]




    print("Showing recommendations for user: {}".format(user_selected))
    print("#######" * 6)
    print("Movies with high ratings from user")
    print("#######" * 6)

    top_movies_user = (movies_watched_by_user.sort_values(by="rating", ascending=False).head(10).movie_id.values)
    #print(top_movies_user)

    lens_rows = lens[lens["movie_id"].isin(top_movies_user)]
    lens_rows = lens_rows.drop_duplicates(subset = ["title"])
    #print(lens3_rows)

    for row in lens_rows.itertuples(): #The itertuples() function is used to iterate over DataFrame rows as namedtuples.
        print(row.title)

    print("#######" * 6)
    print("Top 10 movie recommendations")
    print("#######" * 6)

    recommended_movies = lens[lens["movie_id"].isin(recommended_movie_ids)]
    recommended_movies = recommended_movies.drop_duplicates(subset = ["title"])

    for row in recommended_movies.itertuples():
        print(row.title)

    return render_template('movies.html',user=movies_watched_by_user,movie=recommended_movies)




# #the first row of df lens3.
# user_selected = lens.user_id.sample(3).iloc[2]

# movies_watched_by_user = lens[lens.user_id == user_selected]

# print(movies_watched_by_user)

# movies_not_watched = lens[~lens["movie_id"].isin(movies_watched_by_user.movie_id.values)
# ]["movie_id"]

# movies_not_watched = list(
#     set(movies_not_watched).intersection(set(movie_id.keys()))
# )

# movies_not_watched = [[movie_id.get(x)] for x in movies_not_watched]

# user_encoder = user_id.get(user_selected)

# user_movie_array = np.hstack(
#     ([[user_encoder]] * len(movies_not_watched), movies_not_watched)
# )  #user_movie_array consists of selected_user in userfind and moviefind

# rate = model.predict(user_movie_array)
# ratings = model.predict(user_movie_array).flatten()

# #For any iterable in python [-10:] denotes the indexing of last 10 items of that iterable.
# #[::-1] denotes same list in reverse order
# #returns top 10 max ratings' indices
# top_ratings_indices = ratings.argsort()[-10:][::-1]
# recommended_movie_ids = [
#     id_movie.get(movies_not_watched[x][0]) for x in top_ratings_indices
# ]




# print("Showing recommendations for user: {}".format(user_selected))
# print("#######" * 6)
# print("Movies with high ratings from user")
# print("#######" * 6)

# top_movies_user = (movies_watched_by_user.sort_values(by="rating", ascending=False).head(10).movie_id.values)
# #print(top_movies_user)

# lens_rows = lens[lens["movie_id"].isin(top_movies_user)]
# lens_rows = lens_rows.drop_duplicates(subset = ["title"])
# #print(lens3_rows)

# for row in lens_rows.itertuples(): #The itertuples() function is used to iterate over DataFrame rows as namedtuples.
#     print(row.title)

# print("#######" * 6)
# print("Top 10 movie recommendations")
# print("#######" * 6)

# recommended_movies = lens[lens["movie_id"].isin(recommended_movie_ids)]
# recommended_movies = recommended_movies.drop_duplicates(subset = ["title"])

# for row in recommended_movies.itertuples():
#     print(row.title)
    
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
    
