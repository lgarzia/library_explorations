# %%
import ibis
import pandas as pd

ibis.options.interactive = True
# %%
df = pd.DataFrame(
    [['a', 1, 2], ['b', 3, 4]],
    columns=['one', 'two', 'three'],
    index=[5, 6],
)
df
# %%
t = ibis.memtable(df, name="t")
t
# %%
t.schema()
# %%
