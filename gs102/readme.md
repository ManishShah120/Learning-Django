# Model Inheritance[Abstract Class]

## The base class should subclass `django.db.models.Model`
-   Abstract Base Classes
-   - are usefull when you want to put some common information into a number of models, You write your base class and put `abstract=True` in the Meta class.
-   -
```
        from django.db import models
        class CommonInfo(models.Model):
            name = models.CharField(max_length=70)
            age = models.IntegerField()
            class Meta:
                abstract = True

        class Student(CommonInfo):
            fees = models.IntegerField()

        class Teacher(CommonInfo)
            salary = models.IntegerField()
```
Notes: When you are using related_name or related_query_name in an abstract base class(only), part of the value should contain `%(app_label)s` and `%(class)s`
- `%(class)s` is replaced by the lowercased name of the child class thatthe field is used in.
- `%(app_label)s` is replaced byt eh lowercased name of the app the child class is contained within.
```
        from django.db import models
        class Base(models.Model):
            m2m = models.ManyToManyField(
                OtherModel,
                related_name="%(app_label)s_%(class)s_related",
                related_query_name="%(app_label)s_%(class)ss",
            )
            class Meta:
                abstract = True
```



-   Multi-table Inheritance
-   Proxy Models

