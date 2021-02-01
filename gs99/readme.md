# QuerySet API Aggregation
-   `aggregate()`
Syntax:- aggregate(name=agg_function('field'), name=agg_function('field'))

-   `annotate()`
Syntax:- annotate(name=agg_function('field'), name=agg_function('field')))

---

- `Avg(expression, output_field=None, distinct=False, filter=None, **extra)`
-   - Default alias: <field>_avg
-   - Return type: float if input is int, otherwise same as input field

- `Count(expression, distinct=False, filter=None, **extra)`
-   - Default alias: <field>_count
-   - Return type: int

- `Max(expression, output_field=None, filter=None, **extra)`
-   - Default alias: <field>_max
-   - Return type: same as input field, or output_field is supplied

- `Min(expression, out_field=None, filter=None, **extra)`
-   - Default alias: <field>_min
-   - Return type: same as input field, or output_field if supplied

- `Sum(expression, out_field=None, filter=None, **extra)`
-   - Default alias: <field>_sum
-   - Return type: same as input field, or output_field if supplied

- `StdDev(expression, out_field=None, filter=None, **extra)`
-   - Default alias: <field>_stddev
-   - Return type: same as input field, or output_field if supplied

- `Variance(expression, out_field=None, filter=None, **extra)`
-   - Default alias: <field>_variance
-   - Return type: same as input field, or output_field if supplied
