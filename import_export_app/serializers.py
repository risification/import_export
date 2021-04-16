from csv import DictReader

from rest_framework import serializers
from .models import Document, DocumentField


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class DownloadSerializers(serializers.ModelSerializer):
    class Meta:
        model = DocumentField
        fields = ['file_field']

    def create(self, validated_data):
        file_data = validated_data.pop('file_field')
        document = Document.objects.create(**validated_data)
        for file in file_data:
            document(document=document, **file)
            document.save()
        return file_data
