from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    username=models.CharField(max_length=300,unique=True)
    nickname=models.CharField(max_length=300, null=False)
    def __str__(self):
        return self.username or ''


class Post(models.Model):
    title=models.CharField(max_length=200)
    poster=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    url= models.URLField(max_length=100)
    created= models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['-created']
    def __str__(self):
        return self.title or ''

class Vote(models.Model):
    voter=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.voter)