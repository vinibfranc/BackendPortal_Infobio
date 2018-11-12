from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
from rest_framework import viewsets
from rest_framework import generics
from .models import About, Homepage, AreaBigCategory, SpecificArea, Opportunity
from .forms import OpportunityForm
from .serializers import AboutSerializer, HomepageSerializer, AreaBigCategorySerializer, SpecificAreaSerializer, OpportunitySerializer
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView

def home(request):
    return render(request, 'cms/index.html')


class OpportunityView(SuccessMessageMixin, CreateView):

    template_name = 'cms/add_opportunity.html'
    form_class = OpportunityForm
    success_url = 'adicionar-oportunidade'

    def get_success_message(self, cleaned_data):
        
        return 'Obrigado! A oportunidade foi registrada e estará no site em breve!'

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