# Many to One Relationship
-   When one or more row of table B can be linked to one row of table A.

Eg.:-
```
class User(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()
```
