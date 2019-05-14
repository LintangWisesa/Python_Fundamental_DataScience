# pip install seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

data = sns.load_dataset('flights')
print(data)

# https://github.com/mwaskom/seaborn-data