
Pandera is a must-use library for local DataFrame-based workflows. As an example, I scrape data - does it still meet contract? 
Reinforced idea of hypothesis (aka property based testing in pytest)

[medium](https://medium.com/@seckindinc/dataframe-validation-with-pandera-cacd1a20878f)
[readme](https://pandera.readthedocs.io/en/stable/)
[github](https://github.com/unionai-oss/pandera)

Big Idea <-- Set expectations of DataFrame contract. 

pandera is a Union.ai open source project that provides a flexible and expressive API for performing data validation on dataframe-like objects to make data processing pipelines more readable and robust.

Dataframes contain information that pandera explicitly validates at runtime. This is useful in production-critical data pipelines or reproducible research settings. 

1. Define a schema once
2. Check types and properties of columns
3. perform more statistical validation like hypothesis testing

Integrates via function decorators
Define dataframe models with class-based API
**This is cool** --> Synthesize data from schema objects for property-based testing
Lazily_validate --> check all rules
Integrate --> pydantic, fastapi, mypy

Core Concepts:
* DataFrame Schemas
    * The DataFrameSchema class enables the specification of a schema that verifies the columns and index of a Pandas DataFrame object
* Column Validation
    * default not nullable
    * can coerce data type before validation runs
    * required columns
    * can validate as stand-alone 
    * column regex pattern matching

[Data Synthesis Strategies](https://pandera.readthedocs.io/en/stable/data_synthesis_strategies.html)
