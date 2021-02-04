# Model Manager

Model Manager is used to interact with database

By default, Django add a manager with the name `objects` to every Django model class.
- django.db.models.manager.Manager

## Change Manager Name
```
from dango.db import models
class Student(models.Model)
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    students = models.Manager()
```

Now to query a datbase:-
`student_data = Student.students.all()`
