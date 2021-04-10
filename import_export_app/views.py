from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .admin import DocumentResources
import tablib
from import_export import resources


# Create your views here.


class DocumentView(APIView):
    def get(self, request, *args, **kwargs):
        document = Document.objects.all()
        dataset = DocumentResources().export()
        serializers = DocumentSerializers(document, many=True)
        with open('file.txt', 'wt', encoding='utf-8') as infile:
            infile.writelines(str(dataset))
        return Response(serializers.data)

    '''def post(self, request, *args, **kwargs):
        serializers = DocumentSerializers(user=request.user)
        if serializers.is_valid():
            dataset = DocumentResources().export()'''
