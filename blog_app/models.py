from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #to add author field
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #to give the initial posting date
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #to print post more descriptive way
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})