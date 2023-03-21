from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return f"{self.title}-------{self.date}"
# Create your models here.
