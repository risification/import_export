from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    target = models.CharField(max_length=40)
    # date_expired = models.DateField()


'''class CsvDocument(CsvModel):
    title = CharField()
    text = CharField()
    date = DateField()
    user = IntegerField()
    target = CharField()
    date_expired = CharField()

    class Meta:
        delimiter = ","
'''


class DocumentField(models.Model):
    file_field = models.FileField()
