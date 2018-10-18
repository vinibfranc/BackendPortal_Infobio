from django.shortcuts import render
from django.http import HttpResponse
import datetime

from rest_framework import viewsets
from rest_framework import generics
from .models import Category, Section, Content, Post, Comment
from .serializers import SectionSerializer, CategorySerializer, ContentSerializer, PostSerializer, CommentSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin

def home(request):
    return render(request, 'cms/index.html')

# Generic Content

class SectionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ContentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()

#Posts

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer