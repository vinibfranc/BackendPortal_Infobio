from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
from rest_framework import viewsets
from rest_framework import generics
from .models import About, Homepage, AreaBigCategory, SpecificArea, Opportunity
from .forms import OpportunityForm
from .serializers import AboutSerializer, HomepageSerializer, AreaBigCategorySerializer, SpecificAreaSerializer, OpportunitySerializer
#from rest_framework_extensions.mixins import NestedViewSetMixin
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'cms/index.html')


#ADAPTAR PARA O QUADRO DE OPORTUNIDADES!

'''def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'cms/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'cms/post_detail.html', {'post': post})'''

def add_opportunity(request):
    #post = get_object_or_404(Opportunity)
    if request.method == "POST":
        form = OpportunityForm(request.POST)
        if form.is_valid():
            opportunity = form.save(commit=False)
            opportunity.save()
            #messages.info(request, 'Enviado com sucesso!')
            #messages.success(request, "Enviado com sucesso!")
            return redirect('https://pivettamarcos.github.io/portal-infobio-ufcspa/inicio')
    else:
        form = OpportunityForm()
    return render(request, 'cms/add_opportunity.html', {'form': form})

# Listando informações na API em JSON
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
    queryset = Opportunity.objects.filter(approved=True)
    serializer_class = OpportunitySerializer

class OpportunityDetail(generics.RetrieveAPIView):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer