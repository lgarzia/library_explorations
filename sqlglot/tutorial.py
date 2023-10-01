# %%
import sqlglot

sqlglot.transpile("SELECT EPOCH_MS(1618088028295)", read="duckdb", write="hive")[0]
# %%
sqlglot.transpile("SELECT STRFTIME(x, '%y-%-m-%S')", read="duckdb", write="hive")[0]
# %%
sql = """WITH baz AS (SELECT a, c FROM foo WHERE a = 1) SELECT f.a, b.b, baz.c, CAST("b"."a" AS REAL) d FROM foo f JOIN bar b ON f.a = b.a LEFT JOIN baz ON f.a = baz.a"""
print(sqlglot.transpile(sql, write="spark", identify=True, pretty=True)[0])
# %%
from sqlglot import exp, parse_one

# %%
# print all column references (a and b)
for column in parse_one("SELECT a, b + 1 AS c FROM d").find_all(exp.Column):
    print(column.alias_or_name)
# %%
# find all projections in select statements (a and c)
for select in parse_one("SELECT a, b + 1 AS c FROM d").find_all(exp.Select):
    for projection in select.expressions:
        print(projection.alias_or_name)
# %%
# find all tables (x, y, z)
for table in parse_one("SELECT * FROM x JOIN y JOIN z").find_all(exp.Table):
    print(table.name)
# %%
import sqlglot

sqlglot.transpile("SELECT foo( FROM bar")

# %%
import sqlglot

try:
    sqlglot.transpile("SELECT foo( FROM bar")
except sqlglot.errors.ParseError as e:
    print(e.errors)
# %%
from sqlglot import condition, select

where = condition("x=1").and_("y=1")
select("*").from_("y").where(where).sql()
# %%
from sqlglot import exp, parse_one

expression_tree = parse_one("SELECT a FROM x")
def transformer(node):
    if isinstance(node, exp.Column) and node.name == "a":
        return parse_one("FUN(a)")
    return node

transformed_tree = expression_tree.transform(transformer)
transformed_tree.sql()
# %%
import sqlglot
from sqlglot.optimizer import optimize

print(
    optimize(
        sqlglot.parse_one("""
            SELECT A OR (B OR (C AND D))
            FROM x
            WHERE Z = date '2021-01-01' + INTERVAL '1' month OR 1 = 0
        """),
        schema={"x": {"A": "INT", "B": "INT", "C": "INT", "D": "INT", "Z": "STRING"}}
    ).sql(pretty=True)
)
# %%
from sqlglot import parse_one

print(repr(parse_one("SELECT a + 1 AS z")))
# %%
