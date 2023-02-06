from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(default='1994-09-07')
    email = models.EmailField(db_index=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    time_on = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.first_name

class Sales(models.Model):
    fee = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()