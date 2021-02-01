# QuerySet API Field Lookups

Field lookups are how you specify the meet of an SQL WHERE clause
They're specified as keyword arguments to the QuerySet methods `filter()`, `exclude()`, `get()`
Syntax:- `field_ollkuptype=value`
Example:- `Student.objects.filter(marks__lt='50')`

## Different Types
- `exact`
-   - Eg.:- Student.objects.get(name__exact='sonam')

- `iexact`
-   - Eg.:- Student.objects.get(name__iexact='sonam')

- `contains`
-   - Eg.:- Student.objects.get(name__contains='kumar')

- `icontains`
-   - Eg.:- Student.objects.get(name__icontains='kumar')

- `in`
-   - Eg.:- Student.objects.filter(id_in=[1, 5, 7])

- `gt`
-   - Eg.:- Student.objects.filter(marks__gt=50)

- `gte`
-   - Eg.:- Student.objects.filter(marks__gte=50)

- `lt`
-   - Eg.:- Student.objects.filter(marks__lt=50)

- `lte`
-   - Eg.:- Student.objects.filter(marks__lte=50)

- `startswith`
-   - Eg.:- Student.objects.filter(name__startswith='r')

- `istartswith`
-   - Eg.:- Student.objects.filter(name__istartswith='r')

- `endswith`
-   - Eg.:- Student.objects.filter(name__endswith='j')

- `iendswith`
-   - Eg.:- Student.objects.filter(name__iendswith='j')

- `range`
-   - Eg.:- Student.objects.filter(passdate__range=('2020-04-01', '2020-05-05'))

- `date`
-   - Eg.:- Student.objects.filter(admdatetime__date=date(2020,6,5))
-   - Eg.:- Student.objects.filter(admdatetime__date__gt=date(2020,6,5))

- `year`
-   - Eg.:- Student.objects.filter(pass_date__year=2020)
-   - Eg.:- Student.objects.filter(pass_date__year_gt=2019)

- `month`
-   - Eg.:- Student.objects.filter(passdate__month=6)
-   - Eg.:- Student.objects.filter(passdate__month_gt=5)

- `day`
-   - Eg.:- Student.objects.filter(passdate__day=5)
-   - Eg.:- Student.objects.filter(passdate__day__gt=3)

- `week`
-   - Eg.:- Student.objects.filter(passdate__week=23)
-   - Eg.:- Student.objects.filter(passdate__week__gt=22)

- `week_day`
-   - Eg.:- Student.objects.filter(passdate__week_day=6)
-   - Eg.:- Student.objects.filter(passdate__week_day__gt=5)

- `quarter`
-   - Eg.:- to retrieve entries in the second quarter(April 1 to June 30)
-   - Eg.:- Student.objects.filter(pass_date__quarter=2)

- `time`
-   - Eg.:- Student.objects.filter(admdatetime__time__gt=time(6,000))

- `hour`
-   - Eg.:- Student.objects.filter(admdatetime__hour__gt=50)

- `minute`
-   - Eg.:- Student.objects.filter(admdatetime__minute__gt=50)

- `second`
-   - Eg.:- Student.objects.filter(admdatetime__second__gt=30)

- `isnull`
-   - Eg.:- Student.objects.filter(roll__isnull=False)

- `regex`
-   - Eg.:- iregex
