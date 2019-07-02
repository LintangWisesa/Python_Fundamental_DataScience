# Market Basket Analysis
# pip install mlxtend
# dataset: https://www.kaggle.com/sulmansarwar/transactions-from-a-bakery/version/1
# tutorial: https://towardsdatascience.com/mba-for-breakfast-4c18164ef82b

import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import mlxtend as ml

# read csv file
bread = pd.read_csv("BreadBasket_DMS.csv")
print(bread.head(8))

# ========================================
# What are the “hot” items at BreadBasket?
# ========================================

sns.countplot(
    x = 'Item', 
    data = bread, 
    order = bread['Item'].value_counts().iloc[:10].index
)
plt.xticks(rotation=90)
# plt.show()

# ========================================
# How many items are sold daily?
# ========================================

df = bread.groupby(['Transaction','Item']).size().reset_index(name='count')
basket = (df.groupby(['Transaction', 'Item'])['count']
          .sum().unstack().reset_index().fillna(0)
          .set_index('Transaction'))
#The encoding function
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
basket_sets = basket.applymap(encode_units)

frequent_itemsets = apriori(basket_sets, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift")
rules.sort_values('confidence', ascending = False, inplace = True)
print(rules.head(10))