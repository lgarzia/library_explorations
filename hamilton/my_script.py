import importlib
import logging
import sys

import pandas as pd

from hamilton import driver

logging.basicConfig(stream=sys.stdout)
initial_columns = {  # load from actuals or wherever -- this is our initial data we use as input.
    # Note: these do not have to be all series, they could be scalar inputs.
    'signups': pd.Series([1, 10, 50, 100, 200, 400]),
    'spend': pd.Series([10, 10, 20, 40, 40, 50]),
}
# we need to tell hamilton where to load function definitions from
module_name = 'my_functions'
module = importlib.import_module(module_name) # or we could just do `import my_functions`
dr = driver.Driver(initial_columns, module)  # can pass in multiple modules
# we need to specify what we want in the final dataframe.
output_columns = [
    'spend',  # or module.spend
    'signups',  # or module.signups
    'avg_3wk_spend',  # or module.avg_3wk_spend
    'spend_per_signup',  # or module.spend_per_signup
]
# let's create the dataframe!
# if you only did `pip install sf-hamilton` earlier:
df = dr.execute(output_columns)
# else if you did `pip install "sf-hamilton[visualization]"` earlier:
dr.visualize_execution(output_columns, './my-dag.dot', {})
#print(df)