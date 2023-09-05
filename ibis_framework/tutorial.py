# %%
# %%
import os

import ibis
from ibis import _

os.chdir(r"C:\Users\lgarzia\Documents\GitHub\library_explorations\ibis_framework")
# %%
ibis.options.interactive = True
con = ibis.sqlite.connect("geography.db")
con.tables
# %%
countries = con.tables.countries
countries.head()
# %%
(
countries.filter(_.continent == "AS")
.select("name", "population")
.order_by(_.population)
.limit(5)
)
# %%
import ibis
import pandas as pd

# Create a Pandas DataFrame
data = pd.DataFrame({'column1': [1, 2, 3, 4, 5],
                     'column2': ['A', 'B', 'C', 'D', 'E'],
                     'column3': [10, 20, 30, 40, 50]})

# %%
# Create an Ibis table from the Pandas DataFrame
table = ibis.pandas.connect({'my_table': data}).table('my_table')

# %%
# Define the query expression
expr = table.filter(table.column1 > 3).group_by(table.column2).aggregate(sum=table.column3.sum())

# %%
# Execute the query
result = expr.execute()
# %%
# Print the result
print(result)
# %%
