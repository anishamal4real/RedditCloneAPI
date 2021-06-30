from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = ['name', 'email', 'phone_number']
    USERNAME_FIELD = 'username'
    name=models.CharField(max_length=50, null=False)
    email=models.CharField(max_length=300, null=False)
    phone_number=models.CharField(max_length=300, null=False)
    username= models.CharField(max_length=50, null=False,  unique=True)


class Post(models.Model):
    title=models.CharField(max_length=200)
    poster=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    url= models.URLField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']

class Vote(models.Model):
    voter=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)


