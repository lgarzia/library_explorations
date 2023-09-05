# %%
import ibis

# %%
ibis.options.sql.default_limit = None
# %%
# All tables in Ibis are immutable. To select a subset of a table's columns, or to add new columns, you must produce a new table by means of a projection.
t = ibis.table(
    [('one', 'string'), ('two', 'float'), ('three', 'int32')], 'my_data'
)
# %%
t
# %%
proj = t.select(['two', 'one'])
# %%
type(proj)
# %%
ibis.show_sql(proj)
# %%
mutated = t.mutate(new_col=t.three * 2)
# %%
ibis.show_sql(mutated)
# %%
mutated = t.mutate(two=t.two * 2)
ibis.show_sql(mutated)
# %%
proj = t[t]
ibis.show_sql(proj)
# %%
t.mutate(new_col=t.three * 2)
# %%
proj = t[t, new_col]
ibis.show_sql(proj)
# %%
t2 = ibis.table([('key', 'string'), ('value', 'float')], 'dim_table')
# %%
diff = (t.two - t2.value).name('diff')
joined = t.join(t2, t.one == t2.key)[t, diff]
# %%
ibis.show_sql(joined)
# %%
expr = (
    t.group_by(['one', 'three'])
    .aggregate(the_sum=t.two.sum())
    .group_by('one')
    .aggregate(mad=lambda x: x.the_sum.abs().mean())
)
# %%
ibis.show_sql(expr)
# %%
