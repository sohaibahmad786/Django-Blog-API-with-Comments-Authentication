from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Student
from .models import Register
from .models import Note
from .models import Category
from .models import Products

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Note)
admin.site.register(Register,UserAdmin)
admin.site.register(Student)
# Register your models here.
