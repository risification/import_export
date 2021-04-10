from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.CharField(max_length=40)
    date_expired = models.DateField()
