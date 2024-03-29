from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    hour = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
