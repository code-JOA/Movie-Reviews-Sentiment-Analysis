
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
    
    
    
    
    
    
    