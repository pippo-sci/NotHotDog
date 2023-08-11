from typing import Callable
import pickle
import os

class FeatureStore:

    def __init__(self):
        # open pickle file if exists
        if not os.path.exists('features.pickle'):
            self.features = {}
        else:
            with open('features.pickle', 'rb') as file:
                self.features = pickle.load(file)

    def to_disk(self):
        with open('features.pickle', 'wb') as file:
            pickle.dump(self.features, file)

    def add_feature(self, name: str, feature: Callable):
        self.features[name] = feature

    def get_feature(self, name: str):
        return self.features[name]
    
    def get_features_names(self):
        return self.features.keys()


