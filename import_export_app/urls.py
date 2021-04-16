from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'document', DocFileModelViewSet)

urlpatterns = [
    path('', DocumentView.as_view()),
    path('', include(router.urls)),
    path('export_file/<int:document_id>/', ExportView.as_view()),
]
