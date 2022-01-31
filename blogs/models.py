from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """A post of a personal blog"""
    title = models.CharField(max_length=40)    
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """ Return string representation of the title"""
        return self.title