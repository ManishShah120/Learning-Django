# QuerySet API(Methods that do not return new QuerySet)

## Retrieving a single object
- `.get()`
-   - Eg.:- Student.objects.get(pk=1)

- `.first()`
-   - Eg.:- student_data = Student.objects.first()
-   - Eg.:- student_data = Student.objects.order_by('name').first()

- `.last()`

- `.latest(*fields)`
-   - Eg.:- student_data = Student.objects.latest('pass_date')

- `.earliest(*fields)`
-   - Eg.:- student_data = Student.objects.earliest('pass_date')

- `.exists()`
-   - Eg.:- student_data = Student.objects.all()
-   - print(student_data.exists())

- `.create(**kwargs)`
-   - Eg.:- s = Student.objects.create(name="Sameer", roll=112, city="Bokaro", marks=60, pass_date='2020-5-4')

- `.get_or_create(defaults=None, **kwargs)`
-   - Eg.:- student_data, created = Student.objects.get_or_create(name="Sabirr", roll=113, city="Bookaro", marks=90, pass_date='2020-6-4')

- `.update(**kwargs)`
-   - Eg.:- student_data = Student.objects.filter(id=12).update(name='Kabir', marks=80)

- `.update_or_create(defaults=None, **kwargs)`

- `.bulk_create(objs, batch_size=None, ignore_conflicts=False)`
-   - Eg.:- 
```
            objs = [
                Student(name='Sonal', roll=120, city='Dhanbad', marks=40, pass_date='2020-5-4'),
                Student(name='Kunal', roll=121, city='Dumka', marks=50, pass_date='2020-5-7'),
                Student(name='Anisa', roll=122, city='Giridih', marks=70, pass_date='2020-5-9')
            ]
            student_data = Student.objects.bulk_create(objs)
```

- `.bulk_update(objs, fields, batch_size=None)`
-   - Eg.:-
```
            all_student_data = Student.objects.all()
            for stu in all_student_data:
                stu.city = 'BHEL'
            student_data = Student.objects.bulk_update(all_student_data, ['city'])
```

- `.in_bulk(id_list=None, field_name='pk')`
-   - Eg.:-
```
            student_data = Student.objects.in_bulk([1, 2])
            print(student_data[1].name)
            print()
            student_data1 = Student.objects.in_bulk([])
            print(student_data1)
            print()
            student_data2 = Student.objects.in_buk()
            print(student_data2)
```

- `.delete()`
-   - Eg.:-
```
            # Delete One Record
            student_data = Student.objects.get(pk=13)
            deleted = student_data.delete()

            # Delete in Bulk
            student_data = Student.objects.filter(marks=50).delete()

            # Delete all Records
            student_data = Student.objects.all().delete()
```

- `.count()`
-   - Eg.:-
```
            student_data = Student.objects.all()
            print(student_data.count())
```

- `.explain(format=None, **options)`
-   - Eg.:- print(Student.objects.all().explain())

- `aggregate(*args, **kwargs)`

- `as_manager()`

- `iterator(chunk_size=2000)`
