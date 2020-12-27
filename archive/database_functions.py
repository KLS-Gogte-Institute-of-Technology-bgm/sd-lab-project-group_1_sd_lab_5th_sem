import pandas as pd 

def addUser(user_id,password , confirm_pass,logins):
    if password != confirm_pass:
        return -1
    logins = logins.append({'user_id':user_id , 'password':password} , ignore_index = True)

    return 1
    
    

def authenticate(user_id , password,logins ):
    if user_id not in logins.user_id:
        return -1
        
    else: 
        key = logins[logins.user_id == user_id].password
        if key == password:
            return 1 

        else:
            return -2


def rate(user_id , title , rating , lens, movies):
    if title not in movies:
        return False

    else:
        movie_id = lens[lens['title'] == title].loc(0)
        lens = lens.append({'movie_id':movie_id , 'title':title , 'user_id':user_id, 'rating':rating } , ignore_index = True) 
        return lens

