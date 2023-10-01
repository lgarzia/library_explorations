Overview: It's the most promising SQL parser/generator library to add to my workflow. 

[sqlglot](https://github.com/tobymao/sqlglot)
SQLGlot is a no-dependency SQL parser, transpiler, optimizer, and engine. It can be used to format SQL or translate between 20 different dialects like DuckDB, Presto, Spark, Snowflake, and BigQuery. It aims to read a wide variety of SQL inputs and output syntactically and semantically correct SQL in the targeted dialects.

You can easily customize the parser, analyze queries, traverse expression trees, and programmatically build SQL.

* Transpile from one language to another
You can explore SQL with expression helpers to do things like find columns and tables:

Build and Modify SQL
SQLGlot supports incrementally building sql expressions:

from sqlglot import select, condition
where = condition("x=1").and_("y=1")
select("*").from_("y").where(where).sql()

SQLGlot can rewrite queries into an "optimized" form. It performs a variety of techniques to create a new canonical AST. This AST can be used to standardize queries or provide the foundations for implementing an actual engine.

SQLGlot can calculate the difference between two expressions and output changes in a form of a sequence of actions needed to transform a source expression into a target one:

One can even interpret SQL queries using SQLGlot, where the tables are represented as Python dictionaries.