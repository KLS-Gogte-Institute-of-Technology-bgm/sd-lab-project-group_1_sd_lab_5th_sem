#libraries
import pandas as pd

def load_data():
    print()
    print("Loading Dataset...")

    r_cols = ['user_id','movie_id','rating','unix_timestamp']
    m_cols = ['movie_id','title','release_date','video_release_date','imdb_url','unknown','Action','Adventure','Animation',
          'Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance',
          'Sci-Fi','Thriller','War','Western']

    ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols,encoding='latin-1')
    movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols,encoding='latin-1')

    #merge movies and ratings
    movie_ratings = pd.merge(movies, ratings)

    print("Dataset loaded successfully!")
    print()

    return movie_ratings
