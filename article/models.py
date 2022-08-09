from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    published_in = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
