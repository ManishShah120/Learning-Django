# Custom Model manager

Mainly for two reasons we need
- to modify the initial QuerySet the Manager returns
- to add extra Manager methods


## Modify the initial QuerySet
Eg.:-/Syntax

Write  Model Manger
```
class CustomManager(models.Manager)
    def get_queryset(self):
        return super.get_queryset().order_by('name')
```
Associate Manager with Model
```
class Student(models.Model):
    objects = odels.Manager()
    students = CustomManager()
`views.py`
    Student_data = Student.objects.all()
```
