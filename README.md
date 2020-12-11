[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=286635&assignment_repo_type=GroupAssignmentRepo)

# Movie Recommender System
A recommender system, or a recommendation system (sometimes replacing 'system' with a synonym such as platform or engine), is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item. They are primarily used in commercial applications.

## Overview
**1. The Dataset**
MovieLens 100K Dataset  - https://grouplens.org/datasets/movielens/100k/
    MovieLens data sets were collected by the GroupLens Research Project
at the University of Minnesota.

This data set consists of:
* 100,000 ratings (1-5) from 943 users on 1682 movies.
* Each user has rated at least 20 movies.
* Simple demographic info for the users (age, gender, occupation, zip)

**2.Data Preparation**
    For this project, we will be using the __*u.data*__ and __*u.item*__  dataset. This dataset has all we need to create a movie recommender.

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

## Built with
* Python
## Python Dependencies
* numpy
* pandas
* tensorflow
* matplotlib
* keras

## Authors
* **Nikita Kodkany** - *Aspiring Machine Learning Practioner*
* **Nischal Kanishk** - *Web Developer*
* **Prathamesh Korannae** - *Aspiring Machine Learning Practioner*
* **Prithvi Gudodagi** - *Aspiring Cyber Security Practioner*

## Reference
* Andrew Ng
