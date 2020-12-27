import pandas as pd 
import archive.config as config


def addUser(user_id,password , confirm_pass):
   

    if password != confirm_pass:
        return -1

    if config.logins.user_id.isin([user_id]).any():
        return -2
    config.logins = config.logins.append({'user_id':user_id , 'password':password} , ignore_index = True)

    return 1
    
    

def authenticate(user_id , password):
    if not config.logins.user_id.isin([user_id]).any():
        return -1
        
    else: 

        print(config.logins)
        print(user_id)
        key = config.logins[config.logins.user_id == int(user_id)].password.values
        print(key)
        
        if key == int(password):
            return 1 

        else:
            return -2


def rate(user_id , title , rating):
    
    if title not in config.movies:
        return False

    else:
        movie_id = config.lens[config.lens['title'] == title].loc(0)
        config.lens = config.lens.append({'movie_id':movie_id , 'title':title , 'user_id':user_id, 'rating':rating } , ignore_index = True) 
        

