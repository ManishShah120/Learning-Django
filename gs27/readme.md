# ModelAdmin Class and How to register ModelAdmin Class
- Second Way
```
class StudentAdmin(admin.ModelAdmin):
list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')

admin.site.register(Sutdent, StudentAdmin)
```


- Also decorator
- Register Model by decorator
```
@admin.register(Sutdent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')
```
