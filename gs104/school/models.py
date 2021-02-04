from django.db import models

class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)


class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['city']
