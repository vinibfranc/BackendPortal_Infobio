
from django.urls import include, path
from rest_framework import routers
#from .views import list_info

from cms.views import SectionViewSet, CategoryViewSet, ContentViewSet

router = routers.DefaultRouter()
router.register('section', SectionViewSet, base_name='section')
router.register('category', CategoryViewSet, base_name='category')
router.register('content', ContentViewSet, base_name='content')

urlpatterns = [
    #path('list_info/', list_info, name='list_info'),
    path('', include(router.urls)),
]
