import pandas as pd 

def addUser(user_id):
    pass


def rate(user_id , title , rating , lens, movies):
    if title not in movies:
        return False

    else:
        movie_id = lens[lens['title'] == title].loc(0)
        lens = lens.append({'movie_id':movie_id , 'title':title , 'user_id':user_id, 'rating':rating } , ignore_index = True) 
        return lens

