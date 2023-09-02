# %%
import duckdb

# %%
duckdb.sql('SELECT 42').show()
# This will run queries using an in-memory database that is stored globally inside the Python module. The result of the query is returned as a Relation.
# %%
r1 = duckdb.sql('SELECT 42 AS i')
duckdb.sql('SELECT i * 2 AS k FROM r1').show()
# This is very cool

# %%
duckdb.read_csv('example.csv')  
# %%
duckdb.sql('SELECT * FROM "example.csv"') 
# %%
import pandas as pd

pandas_df = pd.DataFrame({'a': [42]})

# %%
duckdb.sql('SELECT * FROM pandas_df')
# %%
duckdb.sql('SELECT 42').df() 
# %%
