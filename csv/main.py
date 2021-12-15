import pandas as pd
import numpy as np
from read import absolutepath
from calc.operations.addition import Addition


data = pd.read_csv(absolutepath("input/input.csv"))

for idx in data.index:
    numbers = (data['First'][idx], data['Second'][idx])
    addition = Addition(numbers)
    assert addition.get_result() == data['Sum'][idx]
