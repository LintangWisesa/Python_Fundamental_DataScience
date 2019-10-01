import pandas as pd
import numpy as np

df = pd.DataFrame([
    {'x': 12}, {'x': 12}, {'x': 12}
])

# tanpa copy(), df2 & df akan senasib sepenanggungan
# df2 = df
# df2['y'] = [1,2,3]

# dengan copy(), hanya df2 yg punya kolom y
df2 = df.copy()
df2['y'] = [1,2,3]

print(df)
print(df2)