#libraries
import pandas as pd
import numpy as np

from archive.datasetloader import load_data

movie_ratings = load_data()

def datapreprocessor():
    #drop columns that aren't required
    lens = movie_ratings.drop(['release_date','video_release_date','imdb_url','unix_timestamp', 'unknown','Action','Adventure','Animation',
        'Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance',
        'Sci-Fi','Thriller','War','Western'], axis = 1)



    #index all users
    user_ids = lens["user_id"].unique().tolist()
    user_id = {x: i for i, x in enumerate(user_ids)}
    id_user = {i: x for i, x in enumerate(user_ids)}

    #index all movies
    movie_ids = lens["movie_id"].unique().tolist()
    movie_id = {x: i for i, x in enumerate(movie_ids)}
    id_movie = {i: x for i, x in enumerate(movie_ids)}


    #to find the movie and user using their ids
    lens["userfind"] = lens["user_id"].map(user_id)
    lens["moviefind"] = lens["movie_id"].map(movie_id)

    #number of users and number of movies
    num_users = len(id_user)
    num_movies = len(id_movie)

    #to normalize the ratings
    lens["rating"] = lens["rating"].values.astype(np.float32)
    min_rating = min(lens["rating"])
    max_rating = max(lens["rating"])

    print("Number of users: {}".format(num_users))
    print("Number of Movies: {}".format(num_movies))
    print("Min rating: {}".format(min_rating))
    print("Max rating: {}".format(max_rating))
    print()

    #Prepare training and validation data, set seed, normalise rating
    x = lens[["userfind", "moviefind"]].values

    # Normalize the targets between  0 and 1. Makes it easy to train.
    y = lens["rating"].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

    # Assuming training on 75% of the data and validating on 25%.
    train_indices = int(0.75 * lens.shape[0])  #take 75% of the rows as training data

    xtrain, xval, ytrain, yval = (
        x[:train_indices],
        x[train_indices:],
        y[:train_indices],
        y[train_indices:],
    )

    return lens, user_id, num_movies, num_users, xtrain, ytrain, xval, yval, movie_id, id_movie, user_id , id_user


datapreprocessor()
