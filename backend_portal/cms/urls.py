
from django.urls import path
from .views import list_info

urlpatterns = [
    path('', list_info, name='list_info')
]