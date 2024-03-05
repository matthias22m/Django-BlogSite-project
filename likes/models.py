from django.db import models
from Blog.models import Post
from django.contrib.auth.models import User


class LikedItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, default=1)
    
    class Meta:
        unique_together = ('user','post')
    
    def __str__(self):
        return f"'{self.user}' liked '{self.post.title}'"
