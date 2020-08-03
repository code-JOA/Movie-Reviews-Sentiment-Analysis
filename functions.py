# fucntion to replace Missing values ie all Nan in the df with Unknown
def fill_na(data):
    """Iterate through columns , if any nulls replace with "Unkonwn" """
    for col in data.columns:
        if (data[col].isnull().any()):
            if (col):
                data[col].fillna("Unknown", inplace=True)         
    return data

# data = fill_na(data)


def make_genrelist(x):
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