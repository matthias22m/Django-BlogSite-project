from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Catagory(models.Model):
    name = models.CharField(unique=True,max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"'{self.author}' to '{self.post}' "