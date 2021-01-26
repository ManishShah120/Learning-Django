# QuerySet API/ QuerySET API Methods that return new QuerySets

Syntax:- queryset.query

## Methods that return new QuerySets

### Retrieving all objects
- `.all()`
-   - Eg.:- Student.objects.all()

### Retrieving specific objects
- `.filter(**kwargs)`
-   - Eg.:- Student.objects.filter(marks=70)
- `.exclude(**kwargs)`
-   - Eg.:- Student.objects.exclude(marks=70)



- `.order_by(*fields)`
- `.reverse()`
- `.values(*fields, **expressions)`
- `.distinct(*fields)`
- `.values_list(*fields, flat=False, named=False)`

- `.using(alias)`
-   - Eg.:- student_data = Student.objects.using('default')

- `.dates(field, kind, order='ASC')`
- `.datetimes(field_name, kind, order='ASC', tzinfo=None)`

- `.none()`
-   - Eg.:- student_data = Student.objects.none()

- `.union(*other_qs, all=False)`
-   - Eg.:- student_data = qs2.union(qs1, all=True)

- `.intersection(*other_qs)`
- `.difference(*other_qs)`
- `.select_related(*fields)`
- `.defer(*fields)`
- `.only(*fields)`
- `prefetch_related(*lookups)`
- `extra(select=None, where=None, params=None, tables=None, order_by=None, select_params=None)`
- `select_for_update(nowait=False, skip_locked=False, of=())`
- `raw(raw_query, params=None, translation=None)`
- `annotate(*args, **kwargs)`

- `AND(&)`
-   - Eg.:- student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
-   - Eg.:- student_data = Student.objects.filter(id=6, roll=106)
-   - Eg.:- student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

- `OR(|)`
-   - Student.objects.filter(id=11) | Student.objects.filter(roll=106)
-   - Student.objects.filter(Q(id=11)|Q(roll=106))
