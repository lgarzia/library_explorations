# Summary
In memory, Analytics Database
BigQuery -> DuckDB -> runs lots of queries


# Resources
`pip install duckdb`

[DuckDB Getting Started](https://duckdb.org/docs/api/python/overview.html)
DuckDB is an easy-to-use open source in-process OLAP database (that processes data in memory and doesn’t require a dedicated server/service) — described by many in simplified terms as the SQLite equivalent for analytical OLAP workloads.

Chain queries together - use variables as input tables
DuckDB can also directly query Pandas DataFrames, Polars DataFrames and Arrow tables.
By default DuckDB operates on an in-memory database. That means that any tables that are created are not persisted to disk. Using the .connect method a connection can be made to a persistent database. Any data written to that connection will be persisted, and can be reloaded by re-connecting to the same file.

[Gist - BQ 2 DuckDB](https://gist.github.com/ML-engineer/e28ae87e830ca7f8e594bce6ca33e38c)
[Medium - DuckDB](https://medium.com/better-programming/duckdb-whats-the-hype-about-5d46aaa73196)
DuckDB has been on my radar for a while, a columnar SQLLite database. 
The final push was a buddy who recommended I check out DuckDB; 
the fastest way to read and write data and use it in their Data Engineering pipelines.

DuckDB has the capability to analyze data where it might live, e.g. on the laptop or **in the cloud**.

DuckDB is embeddable — like SQLite — and is optimized for analytics. The big deal here is the embeddable part (like a library without bringing in the typical PostgreSQL dependency), eliminating the network latency you usually get when talking to a database.

In concrete terms, this means that you can run DuckDB on a cloud virtual machine, in a cloud function, in the browser, or on your laptop as mentioned prior.
DuckDB on Kubernetes for a zero-copy layer to read S3 in the Data Lake! Inspired by this Tweet. The cheapest and fastest option to get started.

[DB-Engines](https://db-engines.com/en/ranking_trend/system/DuckDB)
[airbyte](https://glossary.airbyte.com/term/duckdb/?fbclid=IwAR35TXxCxK5cmAVuwzD8lGnTbudO6m8NcK_Kyd4q-0l77uxTB5U8_szLHeY)
# Use Cases
Ultra-fast analytical use-case locally
Processing and storing tabular datasets, e.g. from CSV or Parquet files
Doing interactive data analysis, e.g. joining & aggregate multiple large tables
Having concurrent large changes, to multiple large tables, e.g. appending rows, adding/removing/updating columns
Having large result set transfer to client