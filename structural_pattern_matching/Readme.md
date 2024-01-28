https://nedbatchelder.com/blog/202312/realworld_matchcase.html
https://towardsdatascience.com/python-structural-pattern-matching-top-3-use-cases-to-get-you-started-262160007fa0

```
match — The subject you want to evaluate conditions for. It could be a status code returned by an API request.
case — An individual condition evaluated to see if a match is confirmed.
```

```python
match subject:
    case <pattern*1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

Sometimes matching on a single variable just won’t cut it. The good news is — you can throw almost anything imaginable inside Python’s match statement.

You can use structural pattern matching with Python’s classes and data classes. The documentation shows you how to work with data classes, so I’ll cover regular ones here.
