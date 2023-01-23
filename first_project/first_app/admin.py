from django.contrib import admin
from .models import Person
from .models import Sales
# Register your models here.

admin.site.register(Person)
admin.site.register(Sales)