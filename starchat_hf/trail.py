# Trying out hugging face
# %%
def get_item_from_dict(dict, key):
    return dict[key]

print(get_item_from_dict({'a': 1, 'b': 2}, 'a'))

# %%
import pandas as pd

pd.read_csv 'data.csv'
# %%
df = pd.read_csv('data.csv')
df.head()
# %%
def remove_space(col_name: pd.Series):
    return col_name.apply(lambda x: x.strip())

def create_datetime(col_name: pd.Series): 
    pd.to_datetime(col_name)

def hello_world():
    print("hello world")