# Proxy Model Inheritance
Eg.:-/Syntax

```
    from django.db import models

    class ExamCenter(models.Model):
        cname = models.CharField(max_length=70)
        city = models.CharField(max_length=70)


    class MyExamCenter(ExamCenter):
        class Meta:
            proxy = True
            ordering = ['city']

        def do_something(self):
            pass


    class MySome(ExamCenter):
        object = newManager()

        class Meta:
            proxy = True
```

We have see three Tyeps of Model Inheritance
- Abstract Base class Inheritance
- MultiTable Inheritance
- Proxy Model Inheritance
