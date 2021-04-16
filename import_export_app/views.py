from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .admin import DocumentResources
import tablib
from rest_framework import viewsets


# Create your views here.


class DocumentView(APIView):
    def get(self, request, *args, **kwargs):
        document = Document.objects.all()
        dataset = DocumentResources().export()
        serializers = DocumentSerializers(document, many=True)
        with open('media/file.csv', 'wt', encoding='utf-8') as infile:
            infile.writelines(str(dataset.csv))
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = DocumentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"data": "OK"}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors)


from django.core.files import File


class ExportView(APIView):

    def get(self, request, *args, **kwargs):
        document = Document.objects.get(id=kwargs['document_id'])
        serializers = DocumentSerializers(document)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializers = DownloadSerializers(data=request.data)
        if serializers.is_valid():
            return Response({"data": 1})
        return Response(serializers.errors)


class DocFileModelViewSet(viewsets.ModelViewSet):
    serializer_class = DownloadSerializers
    queryset = DocumentField.objects.all()
