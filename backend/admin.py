from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Register
from .models import Post
from .models import Comment

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Register,UserAdmin)
# Register your models here.
