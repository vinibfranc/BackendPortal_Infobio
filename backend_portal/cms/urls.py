
from django.urls import include, path
from cms.api import router
from . import views
#from .views import list_info


urlpatterns = [
    #path('list_info/', list_info, name='list_info'),
    path('', views.home, name='index'),
    path('content/', include(router.urls), name='content'),
    path('tinymce/', include('tinymce.urls')),
    path('post/', views.PostList.as_view(), name='post'),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('comment/', views.CommentList.as_view(), name='comment'),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
]
