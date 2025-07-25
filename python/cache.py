import joblib
import pandas as pd
import json
import os



class Cache:
    """
    Classe pour gérer le cache des datasets
    """

    @staticmethod
    def put_in_cache(df:pd.DataFrame, cache_file:str = 'dataset_cache.pkl'):
        """
        Sauvegarde le dataset dans le cache
        """
        path = os.path.join(os.getcwd(), "drk_stgs/config.json")
        


        with open(path, 'r', encoding="utf-8") as file_r:
            config = json.load(file_r)
        config["cache_file"] = cache_file
        with open(path, 'w+', encoding= "utf-8") as file_w:
            json.dump(config,file_w, indent=4)
        try:
            joblib.dump(df,cache_file)
            file = cache_file
            return True
        except Exception as e:
            return e
        


    @staticmethod
    def load_from_cache():
        """
        Récupére le dataset dans le cache 
        """
        path = os.path.join(os.getcwd(), "drk_stgs/config.json")
        with open(path, 'r', encoding="utf-8") as file_r:
            config = json.load(file_r)
        file = config.get("cache_file", "dataset_cache.pkl")

        data = joblib.load(file)
        return data

