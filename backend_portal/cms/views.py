from django.shortcuts import render
from django.http import HttpResponse
import datetime

from rest_framework import viewsets
from .models import Category, Section, Content
from .serializers import SectionSerializer, CategorySerializer, ContentSerializer

'''def list_info(request):
    agora = datetime.datetime.now()
    html = "<html><body>Testando! Agora é: %s</body></html>" % agora
    return HttpResponse(html)'''

class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()