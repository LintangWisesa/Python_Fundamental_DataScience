# pip install seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

# https://github.com/mwaskom/seaborn-data
data = sns.load_dataset('flights')
print(data)

data = data.pivot('month', 'year', 'passengers')
print(data)