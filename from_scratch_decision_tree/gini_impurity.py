# %%
import pandas as pd

data = [
    {'target':1, 
     'category': 'cat'},
     {'target':1, 
     'category': 'cat'},
     {'target':0, 
     'category': 'cat'},
     {'target':1, 
     'category': 'cat'},
]
df = pd.DataFrame(data)
# %%
df
# %%
probs = df[df['category']=='cat'].value_counts('target', normalize=True)
# %%
1 - sum(probs**2) # even was .5, skewed .375 lower gini impurity
# %%
