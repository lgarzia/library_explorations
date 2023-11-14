```python
import pandas as pd
import pandera as pa

# data to validate
df = pd.DataFrame({
    "column1": [1, 4, 0, 10, 9],
    "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
    "column3": ["value_1", "value_2", "vlue_3", "value_2", "value_1"],
})
```


```python
schema = pa.DataFrameSchema({
    "column1": pa.Column(int, checks=pa.Check.le(10)),
    "column2": pa.Column(float, checks=pa.Check.lt(-1.2)),
    "column3": pa.Column(str, checks=[
        pa.Check.str_startswith("value_"),
        # define custom checks as functions that take a series as input and
        # outputs a boolean or boolean Series
        pa.Check(lambda s: s.str.split("_", expand=True).shape[1] == 2)
    ]),
})
```


```python
validated_df = schema(df)
print(validated_df)
```


    ---------------------------------------------------------------------------

    SchemaError                               Traceback (most recent call last)

    Cell In[6], line 1
    ----> 1 validated_df = schema(df)
          2 print(validated_df)
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\container.py:439, in DataFrameSchema.__call__(self, dataframe, head, tail, sample, random_state, lazy, inplace)
        411 def __call__(
        412     self,
        413     dataframe: pd.DataFrame,
       (...)
        419     inplace: bool = False,
        420 ):
        421     """Alias for :func:`DataFrameSchema.validate` method.
        422 
        423     :param pd.DataFrame dataframe: the dataframe to be validated.
       (...)
        437         otherwise creates a copy of the data.
        438     """
    --> 439     return self.validate(
        440         dataframe, head, tail, sample, random_state, lazy, inplace
        441     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\container.py:371, in DataFrameSchema.validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        359     check_obj = check_obj.map_partitions(  # type: ignore [operator]
        360         self._validate,
        361         head=head,
       (...)
        367         meta=check_obj,
        368     )
        369     return check_obj.pandera.add_schema(self)
    --> 371 return self._validate(
        372     check_obj=check_obj,
        373     head=head,
        374     tail=tail,
        375     sample=sample,
        376     random_state=random_state,
        377     lazy=lazy,
        378     inplace=inplace,
        379 )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\container.py:400, in DataFrameSchema._validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        391 if self._is_inferred:
        392     warnings.warn(
        393         f"This {type(self)} is an inferred schema that hasn't been "
        394         "modified. It's recommended that you refine the schema "
       (...)
        397         UserWarning,
        398     )
    --> 400 return self.get_backend(check_obj).validate(
        401     check_obj,
        402     schema=self,
        403     head=head,
        404     tail=tail,
        405     sample=sample,
        406     random_state=random_state,
        407     lazy=lazy,
        408     inplace=inplace,
        409 )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:97, in DataFrameSchemaBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
         92 components = self.collect_schema_components(
         93     check_obj, schema, column_info
         94 )
         96 # run the checks
    ---> 97 error_handler = self.run_checks_and_handle_errors(
         98     error_handler,
         99     schema,
        100     check_obj,
        101     column_info,
        102     sample,
        103     components,
        104     lazy,
        105     head,
        106     tail,
        107     random_state,
        108 )
        110 if error_handler.collected_errors:
        111     if getattr(schema, "drop_invalid_rows", False):
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:172, in DataFrameSchemaBackend.run_checks_and_handle_errors(self, error_handler, schema, check_obj, column_info, sample, components, lazy, head, tail, random_state)
        161         else:
        162             error = SchemaError(
        163                 schema,
        164                 data=check_obj,
       (...)
        170                 reason_code=result.reason_code,
        171             )
    --> 172         error_handler.collect_error(
        173             result.reason_code,
        174             error,
        175             original_exc=result.original_exc,
        176         )
        178 return error_handler
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:192, in DataFrameSchemaBackend.run_schema_component_checks(self, check_obj, schema_components, lazy)
        190 for schema_component in schema_components:
        191     try:
    --> 192         result = schema_component.validate(
        193             check_obj, lazy=lazy, inplace=True
        194         )
        195         check_passed.append(is_table(result))
        196     except SchemaError as err:
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\components.py:169, in Column.validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        142 def validate(
        143     self,
        144     check_obj: pd.DataFrame,
       (...)
        150     inplace: bool = False,
        151 ) -> pd.DataFrame:
        152     """Validate a Column in a DataFrame object.
        153 
        154     :param check_obj: pandas DataFrame to validate.
       (...)
        167     :returns: validated DataFrame.
        168     """
    --> 169     return self.get_backend(check_obj).validate(
        170         check_obj,
        171         self,
        172         head=head,
        173         tail=tail,
        174         sample=sample,
        175         random_state=random_state,
        176         lazy=lazy,
        177         inplace=inplace,
        178     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:119, in ColumnBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
        115             check_obj = validate_column(
        116                 check_obj, column_name, return_check_obj=True
        117             )
        118         else:
    --> 119             validate_column(check_obj, column_name)
        121 if lazy and error_handler.collected_errors:
        122     raise SchemaErrors(
        123         schema=schema,
        124         schema_errors=error_handler.collected_errors,
        125         data=check_obj,
        126     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:89, in ColumnBackend.validate.<locals>.validate_column(check_obj, column_name, return_check_obj)
         84         error_handler.collect_error(
         85             reason_code=None,
         86             schema_error=err,
         87         )
         88 except SchemaError as err:
    ---> 89     error_handler.collect_error(err.reason_code, err)
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:68, in ColumnBackend.validate.<locals>.validate_column(check_obj, column_name, return_check_obj)
         65 def validate_column(check_obj, column_name, return_check_obj=False):
         66     try:
         67         # pylint: disable=super-with-arguments
    ---> 68         validated_check_obj = super(ColumnBackend, self).validate(
         69             check_obj,
         70             copy(schema).set_name(column_name),
         71             head=head,
         72             tail=tail,
         73             sample=sample,
         74             random_state=random_state,
         75             lazy=lazy,
         76             inplace=inplace,
         77         )
         79         if return_check_obj:
         80             return validated_check_obj
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\array.py:69, in ArraySchemaBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
         66     error_handler.collect_error(exc.reason_code, exc)
         68 # run the core checks
    ---> 69 error_handler = self.run_checks_and_handle_errors(
         70     error_handler,
         71     schema,
         72     check_obj,
         73     head,
         74     tail,
         75     sample,
         76     random_state,
         77 )
         79 if lazy and error_handler.collected_errors:
         80     if getattr(schema, "drop_invalid_rows", False):
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\array.py:150, in ArraySchemaBackend.run_checks_and_handle_errors(self, error_handler, schema, check_obj, head, tail, sample, random_state)
        139         else:
        140             error = SchemaError(
        141                 schema=schema,
        142                 data=check_obj,
       (...)
        148                 reason_code=result.reason_code,
        149             )
    --> 150             error_handler.collect_error(
        151                 result.reason_code,
        152                 error,
        153                 original_exc=result.original_exc,
        154             )
        156 return error_handler
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    SchemaError: <Schema Column(name=column3, type=DataType(str))> failed element-wise validator 0:
    <Check str_startswith: str_startswith('value_')>
    failure cases:
       index failure_case
    0      2       vlue_3



```python
from pandera.typing import Series

class Schema(pa.DataFrameModel):

    column1: int = pa.Field(le=10)
    column2: float = pa.Field(lt=-1.2)
    column3: str = pa.Field(str_startswith="value_")

    @pa.check("column3")
    def column_3_check(cls, series: Series[str]) -> Series[bool]:
        """Check that column3 values have two elements after being split with '_'"""
        return series.str.split("_", expand=True).shape[1] == 2

Schema.validate(df)
```


    ---------------------------------------------------------------------------

    SchemaError                               Traceback (most recent call last)

    Cell In[7], line 14
         11         """Check that column3 values have two elements after being split with '_'"""
         12         return series.str.split("_", expand=True).shape[1] == 2
    ---> 14 Schema.validate(df)
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\model.py:306, in DataFrameModel.validate(cls, check_obj, head, tail, sample, random_state, lazy, inplace)
        291 @classmethod
        292 @docstring_substitution(validate_doc=DataFrameSchema.validate.__doc__)
        293 def validate(
       (...)
        301     inplace: bool = False,
        302 ) -> DataFrameBase[TDataFrameModel]:
        303     """%(validate_doc)s"""
        304     return cast(
        305         DataFrameBase[TDataFrameModel],
    --> 306         cls.to_schema().validate(
        307             check_obj, head, tail, sample, random_state, lazy, inplace
        308         ),
        309     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\container.py:371, in DataFrameSchema.validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        359     check_obj = check_obj.map_partitions(  # type: ignore [operator]
        360         self._validate,
        361         head=head,
       (...)
        367         meta=check_obj,
        368     )
        369     return check_obj.pandera.add_schema(self)
    --> 371 return self._validate(
        372     check_obj=check_obj,
        373     head=head,
        374     tail=tail,
        375     sample=sample,
        376     random_state=random_state,
        377     lazy=lazy,
        378     inplace=inplace,
        379 )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\container.py:400, in DataFrameSchema._validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        391 if self._is_inferred:
        392     warnings.warn(
        393         f"This {type(self)} is an inferred schema that hasn't been "
        394         "modified. It's recommended that you refine the schema "
       (...)
        397         UserWarning,
        398     )
    --> 400 return self.get_backend(check_obj).validate(
        401     check_obj,
        402     schema=self,
        403     head=head,
        404     tail=tail,
        405     sample=sample,
        406     random_state=random_state,
        407     lazy=lazy,
        408     inplace=inplace,
        409 )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:97, in DataFrameSchemaBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
         92 components = self.collect_schema_components(
         93     check_obj, schema, column_info
         94 )
         96 # run the checks
    ---> 97 error_handler = self.run_checks_and_handle_errors(
         98     error_handler,
         99     schema,
        100     check_obj,
        101     column_info,
        102     sample,
        103     components,
        104     lazy,
        105     head,
        106     tail,
        107     random_state,
        108 )
        110 if error_handler.collected_errors:
        111     if getattr(schema, "drop_invalid_rows", False):
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:172, in DataFrameSchemaBackend.run_checks_and_handle_errors(self, error_handler, schema, check_obj, column_info, sample, components, lazy, head, tail, random_state)
        161         else:
        162             error = SchemaError(
        163                 schema,
        164                 data=check_obj,
       (...)
        170                 reason_code=result.reason_code,
        171             )
    --> 172         error_handler.collect_error(
        173             result.reason_code,
        174             error,
        175             original_exc=result.original_exc,
        176         )
        178 return error_handler
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\container.py:192, in DataFrameSchemaBackend.run_schema_component_checks(self, check_obj, schema_components, lazy)
        190 for schema_component in schema_components:
        191     try:
    --> 192         result = schema_component.validate(
        193             check_obj, lazy=lazy, inplace=True
        194         )
        195         check_passed.append(is_table(result))
        196     except SchemaError as err:
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\api\pandas\components.py:169, in Column.validate(self, check_obj, head, tail, sample, random_state, lazy, inplace)
        142 def validate(
        143     self,
        144     check_obj: pd.DataFrame,
       (...)
        150     inplace: bool = False,
        151 ) -> pd.DataFrame:
        152     """Validate a Column in a DataFrame object.
        153 
        154     :param check_obj: pandas DataFrame to validate.
       (...)
        167     :returns: validated DataFrame.
        168     """
    --> 169     return self.get_backend(check_obj).validate(
        170         check_obj,
        171         self,
        172         head=head,
        173         tail=tail,
        174         sample=sample,
        175         random_state=random_state,
        176         lazy=lazy,
        177         inplace=inplace,
        178     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:119, in ColumnBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
        115             check_obj = validate_column(
        116                 check_obj, column_name, return_check_obj=True
        117             )
        118         else:
    --> 119             validate_column(check_obj, column_name)
        121 if lazy and error_handler.collected_errors:
        122     raise SchemaErrors(
        123         schema=schema,
        124         schema_errors=error_handler.collected_errors,
        125         data=check_obj,
        126     )
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:89, in ColumnBackend.validate.<locals>.validate_column(check_obj, column_name, return_check_obj)
         84         error_handler.collect_error(
         85             reason_code=None,
         86             schema_error=err,
         87         )
         88 except SchemaError as err:
    ---> 89     error_handler.collect_error(err.reason_code, err)
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\components.py:68, in ColumnBackend.validate.<locals>.validate_column(check_obj, column_name, return_check_obj)
         65 def validate_column(check_obj, column_name, return_check_obj=False):
         66     try:
         67         # pylint: disable=super-with-arguments
    ---> 68         validated_check_obj = super(ColumnBackend, self).validate(
         69             check_obj,
         70             copy(schema).set_name(column_name),
         71             head=head,
         72             tail=tail,
         73             sample=sample,
         74             random_state=random_state,
         75             lazy=lazy,
         76             inplace=inplace,
         77         )
         79         if return_check_obj:
         80             return validated_check_obj
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\array.py:69, in ArraySchemaBackend.validate(self, check_obj, schema, head, tail, sample, random_state, lazy, inplace)
         66     error_handler.collect_error(exc.reason_code, exc)
         68 # run the core checks
    ---> 69 error_handler = self.run_checks_and_handle_errors(
         70     error_handler,
         71     schema,
         72     check_obj,
         73     head,
         74     tail,
         75     sample,
         76     random_state,
         77 )
         79 if lazy and error_handler.collected_errors:
         80     if getattr(schema, "drop_invalid_rows", False):
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\backends\pandas\array.py:150, in ArraySchemaBackend.run_checks_and_handle_errors(self, error_handler, schema, check_obj, head, tail, sample, random_state)
        139         else:
        140             error = SchemaError(
        141                 schema=schema,
        142                 data=check_obj,
       (...)
        148                 reason_code=result.reason_code,
        149             )
    --> 150             error_handler.collect_error(
        151                 result.reason_code,
        152                 error,
        153                 original_exc=result.original_exc,
        154             )
        156 return error_handler
    

    File c:\Users\lgarzia\Documents\GitHub\library_explorations\duckdb\venv\lib\site-packages\pandera\error_handlers.py:38, in SchemaErrorHandler.collect_error(self, reason_code, schema_error, original_exc)
         31 """Collect schema error, raising exception if lazy is False.
         32 
         33 :param reason_code: string representing reason for error.
         34 :param schema_error: ``SchemaError`` object.
         35 :param original_exc: original exception associated with the SchemaError.
         36 """
         37 if not self._lazy:
    ---> 38     raise schema_error from original_exc
         40 # delete data of validated object from SchemaError object to prevent
         41 # storing copies of the validated DataFrame/Series for every
         42 # SchemaError collected.
         43 del schema_error.data
    

    SchemaError: <Schema Column(name=column3, type=DataType(str))> failed element-wise validator 0:
    <Check str_startswith: str_startswith('value_')>
    failure cases:
       index failure_case
    0      2       vlue_3



```python

```
