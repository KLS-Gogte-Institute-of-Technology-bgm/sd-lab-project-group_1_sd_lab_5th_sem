import pandas as pd
from archive.datapreprocessor import datapreprocessor
lens, user_id, num_movies, num_users, xtrain, ytrain, xval, yval , movie_id ,id_movie , user_id , id_user  = datapreprocessor()

movies = lens['title'].unique()

#lens = rate(1 , "Sliding Doors (1998)" , 5 , lens , movies)
logins = [[i+1,i+1] for i in range(943)]
logins = pd.DataFrame(logins , columns = ['user_id','password'])

print("done")