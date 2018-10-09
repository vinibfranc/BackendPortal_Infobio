
from django.urls import include, path
from .api import router
#from .views import list_info


urlpatterns = [
    #path('list_info/', list_info, name='list_info'),
    path('', include(router.urls)),
    path('tinymce/', include('tinymce.urls')),
]
