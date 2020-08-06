
# fucntion to replace Missing values ie all Nan in the df with Unknown
def fill_na(data):
    """Iterate through columns , if any nulls replace with "Unkonwn" """
    for col in data.columns:
        if (data[col].isnull().any()):
            if (col):
                data[col].fillna("Unknown", inplace=True)         
    return data

# data = fill_na(data)


import numpy as np
import pandas as pd


def Make_genrelist(x):

    gen = []
    st = " "
    for i in x:
        if i.get("name") == "Science Fiction":
            scifi = "Sci-Fi"
            gen.append(scifi)
        else:
            gen.append(i.get("name"))
    if gen == []:
        return np.NaN
    else:
        return (st.join(gen))

    

def get_1st_actor(x):
    """get first actor from list of casts """  

    casts=[]
    for i in x:
        casts.append(i.get("name"))
    if casts == []:
        return np.NaN
    else:
        return (casts[0])


def get_2nd_actor(x):
    """get second actor from list of casts """  

    casts=[]
    for i in x:
        casts.append(i.get("name"))
    if casts == [] or len(casts)<=1:
        return np.NaN
    else:
        return (casts[1])


def get_3rdactor(x):
    """get third actor from list of casts """  
    casts=[]
    for i in x:
        casts.append(i.get("name"))
    if casts == [] or len(casts)<=2:
        return np.NaN
    else:
        return (casts[2])

    

def get_directors(x):
    directors = []
    st = ""
    for i in x:
        if i.get("job") == "Director":
            directors.append(i.get("name"))
    if directors == []:
        return np.NaN
    else:
        return (st.join(directors))

    

import requests
import json
from tmdbv3api import TMDb
from tmdbv3api import Movie
tmdb = TMDb()
tmdb.api_key = "de0b39d4bd85599f2e0dbce743bb0857"

tmdb_movie = Movie()
def Get_genre(x):
    genres = []
    result = tmdb_movie.search(x)
    movie_id = result[0].id
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id,tmdb.api_key))
    data_json = response.json()
    if data_json['genres']:
        genre_str = " " 
        for i in range(0,len(data_json['genres'])):
            genres.append(data_json['genres'][i]['name'])
        return genre_str.join(genres)
    else:
        np.NaN    


# +
# custom function for 2018 data
# -

def Get_director(x):
    """This is a custom function to get list of directors from the 2018 data"""
    if " (director)" in x:
        return x.split(" (director)")[0]
    elif " (directors)" in x:
        return x.split(" (directors)")[0]
    else:
        return x.split(" (director/screenplay)")[0]



# +
# Leading actor
# -

def get_actor1(x):
    return ((x.split("screenplay); ")[-1]).split(", ")[0])



# +
# Supporting actor
# -

def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 2:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[1])



# +
# 3rd actor
# -

def get_actor2(x):
    if len((x.split("screenplay); ")[-1]).split(", ")) < 3:
        return np.NaN
    else:
        return ((x.split("screenplay); ")[-1]).split(", ")[2])


