import pandas as pd 
import archive.config as config


def addUser(user_id,password , confirm_pass):
   

    if password != confirm_pass:
        return -1

    if user_id in config.logins.user_id:
        return -2
    config.logins = config.logins.append({'user_id':user_id , 'password':password} , ignore_index = True)

    return 1
    
    

def authenticate(user_id , password):
    if user_id not in config.logins.user_id:
        return -1
        
    else: 
        key = config.logins[config.logins.user_id == user_id].password
        if key == password:
            return 1 

        else:
            return -2


def rate(user_id , title , rating):
    
    if title not in config.movies:
        return False

    else:
        movie_id = config.lens[config.lens['title'] == title].loc(0)
        config.lens = config.lens.append({'movie_id':movie_id , 'title':title , 'user_id':user_id, 'rating':rating } , ignore_index = True) 
        

