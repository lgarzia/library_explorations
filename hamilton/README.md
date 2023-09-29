It's a brilliant piece of engineering. Very clever. 

[github repo](https://github.com/dagworks-inc/hamilton)

The general purpose micro-orchestration framework for creating dataflows from python functions! 
That is, your single tool to express things like data, ML, LLM pipelines/workflows, and even web request logic!

[Basics](https://github.com/DAGWorks-Inc/hamilton/blob/main/basics.md)

Hamilton Functions.
Hamilton Functions are what you, the end user write. Key idea is name of column. 

Hamilton Driver.
Once you've written your functions, you will need to use the Hamilton Driver to build the DAG and orchestrate execution.

We use the following terms interchangeably, e.g. a ____ in Hamilton is ... :
    column
    variable
    node
    function

makes full use of the python type-hint system. 
in Hamilton, as it allows us to type-check the inputs and outputs to match with upstream producers and downstream consumers. 

Functions that start with _ are ignored, and not included in the DAG. Hamilton tries to make use of every function in a module, so this allows us to easily indicate helper functions that won't become part of the DAG.

[Decorators](https://github.com/DAGWorks-Inc/hamilton/blob/main/decorators.md)
[pypi](https://pypi.org/project/sf-hamilton/)