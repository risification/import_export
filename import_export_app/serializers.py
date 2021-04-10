from rest_framework import serializers
from .models import *


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'title', 'text', 'date', 'user', 'target', 'date_expired']


