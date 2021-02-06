# Model Relationship and One to One Relationship
-   One to One Relationship
-   Many to One Relationship
-   Many to Many Relationships

## One to One Relationship
Syntax:- `OneToOneField(to, on_delete, parent_link=False, **options)`
Where,
- `to` - The class to which the model is related.
- `on_delete` - When an object referenced by a ForeignKey is deleted, Django will emulate teh behavior of the SQL constraint specified by the `on_delete` argument. `on_delete` doesn't create an SQL constraint in the database.
- `parent_link`
- `limit_choices_to`
- `related_name`
- `related_query_name`
- `to_field`
- `swappable`
- `db_constraint`

### `on_delete`
- `CASCADE`
- `PROTECT`
- `SET_NULL`
- `SET_DEFAULT`
- `SET()`
- `DO_NOTHING`

Example:-
```
class User(models.Model):
    user_name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

class Page(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
```


Note: Learn't how to implemt signal and do work
