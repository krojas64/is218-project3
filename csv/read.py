import os

import pandas as pd

class Read:
    @staticmethod
    def dataframe_from_csv(filename):
        return pd.read_csv(os.path.abspath(filename))