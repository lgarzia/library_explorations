# Summary
The exciting idea is to write once and deploy to multiple back-ends. 
It would look like Pandas, DuckDB, BigQuery & PySpark. I could work out the logic on a small sample of data and then deploy. I will invest more time in the office exploring use cases and develop richer understanding.

[ibis-framework](https://pypi.org/project/ibis-framework/)
Ibis has three primary components:

* A dataframe API for Python. Python users can write Ibis code to manipulate tabular data.
* Interfaces to 15+ query engines. Wherever data is stored, people can use Ibis as their API of choice to communicate with any of those query engines.
* Deferred execution. Ibis uses deferred execution, so execution of code is pushed to the query engine. Users can execute at the speed of their backend, not their local computer.

`pip install 'ibis-framework[duckdb]'`


[Ibis Docs](https://ibis-project.org/)


[Ibis Docs - Tutorial for SQL](https://ibis-project.org/tutorial/ibis-for-sql-users/#ibis-for-sql-users)
Type-checked and validated as you go. No more debugging cryptic database errors; Ibis catches your mistakes right away.
Easier to write. Pythonic function calls with tab completion in IPython.
More composable. Break complex queries down into easier-to-digest pieces
Easier to reuse. Mix and match Ibis snippets to create expressions tailored for your analysis.

[Ibis Docs - Tutorial for Pandas](https://ibis-project.org/tutorial/ibis-for-pandas-users/#install)
Another difference between Ibis tables and pandas DataFrames are that many of the pandas DataFrame operations do in-place operations (they are "mutable"), whereas Ibis table operations always return a new table expression ("immutable").

[Medium - Intro](https://medium.com/@martin.jurado.p/what-is-ibis-and-how-does-it-help-data-engineering-7a73b1268228)

Additional functionality: Ibis offers additional functionality beyond basic SQL queries, such as data manipulation, aggregation, filtering, statistical calculations and schema management. This allows data engineers to perform common data engineering tasks more easily and efficiently.

[Medium - Tutorial](https://medium.com/towards-data-science/an-introduction-to-ibis-for-python-programmers-2112ea32370d)


[Medium - Older Article](https://medium.com/towards-data-science/ibis-a-framework-to-tie-together-development-and-production-code-588d05e07d11)
