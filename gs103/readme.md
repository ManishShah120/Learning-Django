# Multi-table Inheritance

- In this inheritance each mmodel have their own database table, which means base class and child class will have their own table.
- The inheritace relationship introduces links between the child model and each of its parents(via an automaticallly-created OneToOneField)
- Eg.:-
```
        from django.db import models
        class ExamCenter(models.Model)
            cname = models.CharField(max_length=70)
            city = models.CharField(max_length=70)

        class Student(ExamCenter):
            name = models.CharField(max_length=70)
            roll = models.IntegerField()
```
All of the fields of ExamCenter will also be available in Student, although the data will reside in a different database table.
