# Many to Many Relationship
-   When one row of table `A`  can be linked to one or more rows of table `B`, and vice-versa

Eg.:-
```
class user(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)


class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=70)
    son_duration = models.IntegerField()
```
