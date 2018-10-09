from django.shortcuts import render
from django.http import HttpResponse
import datetime

from rest_framework import viewsets
from .models import Category, Section, Content
from .serializers import SectionSerializer, CategorySerializer, ContentSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin

'''def list_info(request):
    agora = datetime.datetime.now()
    html = "<html><body>Testando! Agora é: %s</body></html>" % agora
    return HttpResponse(html)'''

class SectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ContentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()