import joblib
import pandas as pd





def put_in_cache(df:pd.Dataframe, cache_file:str = 'dataset_cache.pkl'):
    """
    Sauvegarde le dataset dans le cache
    """
    global file
    try:
        joblib.dump(df,cache_file)
        file = cache_file
        return True
    except Exception as e:
        return e
    



def load_from_cache():
    """
    Récupére le dataset dans le cache 
    """
    global file
    data = joblib.load(file)
    return data

