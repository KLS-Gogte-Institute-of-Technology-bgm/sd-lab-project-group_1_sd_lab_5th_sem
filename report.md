# Movie Recommender System
## Introduction
A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item. They are primarily used in commercial applications.

## Collaborative Filtering - Movie Recommendation Systems
With collaborative filtering, the system is based on past interactions between users and movies. With this in mind, the input for a collaborative filtering system is made up of past data of user interactions with the movies they watch.

## Our Project
We built a Movie Recommender System such it is open to any user to either login or create a new account. Once the credentials are accounted for, he/she is given a list of movies to select from. This way he/she can also rate the selected movie and once he/she has finished watching the movie it is added to the watched movie list. Hence the recommended list is updated with a new set for the user.

### Project Artifacts
#### Use-Case Diagram
![Use Case diagram](https://user-images.githubusercontent.com/50879589/103168609-0f85ad80-484e-11eb-9be7-3742ef847db8.png)

#### Sequence Diagram
![Sequence Diagram](https://user-images.githubusercontent.com/50879589/103168606-01379180-484e-11eb-972f-6e5f5d921b54.png)

#### Activity Diagram
![Activity Diagram](https://user-images.githubusercontent.com/50879589/103168599-f3820c00-484d-11eb-8e0c-b0d85939dff2.png)

## Overview
### Built with
* Python
* HTML

### Python Dependencies
* NumPy
* pandas
* TensorFlow
* matplotlib
* Keras
* Flask

### The Dataset
MovieLens 100K Dataset  - https://grouplens.org/datasets/movielens/100k/
    MovieLens data sets were collected by the GroupLens Research Project
at the University of Minnesota.

This data set consists of:
* 100,000 ratings (1-5) from 943 users on 1682 movies.
* Each user has rated at least 20 movies.
* Simple demographic info for the users (age, gender, occupation, zip)

### Data Preparation
For this project, we will be using the __*u.data*__ and __*u.item*__  dataset. This dataset has all we need to create a movie recommender.

 __*u.data*__
The full u.data set, 100000 ratings by 943 users on 1682 items. Each user has rated at least 20 movies.  Users and items are numbered consecutively from 1.  The data is randomly ordered. This is a tab separated list user id | item id | rating | timestamp.
time stamps are unix seconds since 1/1/1970 UTC   

__*u.item*__
Information about the items (movies); this is a tab separated list of movie id | movie title | release date | video release date |IMDb URL | unknown | Action | Adventure | Animation |Children's | Comedy | Crime | Documentary | Drama | Fantasy |Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |Thriller | War | Western.
The last 19 fields are the genres, a 1 indicates the movie is of that genre, a 0 indicates it is not; movies can be in several genres at once. The movie ids are the ones used in the u.data data set.

### Model Used – Neural Network Based Collaborative Filtering
##### Data Preprocesssing
*	The data file that consists of users, movies, ratings and timestamp is read into a pandas dataframe for data preprocessing.
*	Movies and users need to be enumerated to be used for modeling.
*	Variables with the total number of unique users and movies in the data are created, and then mapped back to the movie id and user id.
*	The minimum and maximum ratings present in the data are found.
*	Ratings are then normalized for ease of training the model.

##### Model Building
*	Embeddings are used to represent each user and each movie in the adta.
*	These embeddings will be of vectors size n that are fit bu the model to capture the interation of each user/movie,
*	Both the users and movies are embedded into 50-dimentional (n=50) array vectors for use in the training and test data. Training is carried out on 75% of the data and testing on 25% of the data.
*	To capture the user-movie interaction, the dot product between the user vector and the movie vector is computed to get a predicted rating.
*	The Adam optimizer is used to minimize the accuracy losses between the predicted values and the actual test values.

### Results
A Good Fit!
![MAE](https://user-images.githubusercontent.com/50879589/103168626-3a700180-484e-11eb-85c5-fd66d97f6d7f.png)

1. The plot of training loss decreasesto a point of stability
2. The plot ofvalidation loss decreases to a point of stability and has a small gap with the training loss

## Understanding The Repository
### *archive* (directory)
This directory contains the utility scripts.
1. **datapreprocessor.py** - Script that preprocesses the data that is required to feed into the Neural Network Model and other function. The values are taken from **datasetloader.py**.
2. **datasetloader.py** - Script that loads the data from the directory **ml-100k**.
### *ml-100k*
Directory that contains all the dataset. Downloaded from MovieLens (https://grouplens.org/datasets/movielens/)
### *driver.py*
Script that contains interface that recommends movies for a random user.
### *network.py*
Script that contains the neural network model that is used to drive the recommendations.
### *__pycache__*
Folder containing Python 3 bytecode compiled and ready to be executed. To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc, where the version encodes the format of the compiled file; it generally contains the Python version number.

## Conclusion
We were successfull in building a Movie Recommender System.

## Authors
* **Nikita Kodkany** - 2GI18CS082
* **Nischal Kanishk** - 2GI18CS083
* **Prathamesh Korannae** - 2GI18CS095
* **Prithvi Gudodagi** - 2GI18CS102
