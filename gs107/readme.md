#  Add extra Manager methods

_Write Model manager_
```
class CustomManager(models.Manager):
def get_stu_roll_range(self, r1, r2):
    return super().get_queryset().filter(roll__range=(r1, r2))
```

_Associate Manger with Model_
```
class Student(models.Model):
    objects = models.mnger()
    students = Custommanger()
# `views.py` file

student_data = Student.objects.all()
student_data = Student.students.get_stu_roll_range(101, 103)

```
