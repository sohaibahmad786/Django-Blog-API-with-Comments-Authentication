from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings



class Student(models.Model):
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    course=models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# _________________________ Register Note ________________________
class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    
class Note(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE)
    title=models.CharField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
# _________________ Product API ________________
class Category(models.Model):
    name=models.CharField()

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products'
    )
    name=models.CharField()
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='products/',null=True, blank=True)
    stock=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ____________________ Blog _________________
class Post(models.Model):
    title=models.CharField()
    content=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

# Create your models here.
