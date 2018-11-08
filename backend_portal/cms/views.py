from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
from rest_framework import viewsets
from rest_framework import generics
from .models import About, Homepage, AreaBigCategory, SpecificArea, Opportunity
#from .forms import PostForm, CommentForm
from .serializers import AboutSerializer, HomepageSerializer, AreaBigCategorySerializer, SpecificAreaSerializer, OpportunitySerializer
#from rest_framework_extensions.mixins import NestedViewSetMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'cms/index.html')


#ADAPTAR PARA O QUADRO DE OPORTUNIDADES!

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'cms/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'cms/post_detail.html', {'post': post})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'cms/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

# Listando na API com JSON
class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class AboutDetail(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class HomepageList(generics.ListAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer

class HomepageDetail(generics.RetrieveAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer

class AreaBigCategoryList(generics.ListAPIView):
    queryset = AreaBigCategory.objects.all()
    serializer_class = AreaBigCategorySerializer

class AreaBigCategoryDetail(generics.RetrieveAPIView):
    queryset = AreaBigCategory.objects.all()
    serializer_class = AreaBigCategorySerializer

class SpecificAreaList(generics.ListAPIView):
    queryset = SpecificArea.objects.all()
    serializer_class = SpecificAreaSerializer

class SpecificAreaDetail(generics.RetrieveAPIView):
    queryset = SpecificArea.objects.all()
    serializer_class = SpecificAreaSerializer

class OpportunityList(generics.ListAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class OpportunityDetail(generics.RetrieveAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer