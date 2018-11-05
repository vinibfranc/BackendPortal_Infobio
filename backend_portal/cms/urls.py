
from django.urls import include, path
#from cms.api import router
from . import views
#from .views import list_info


urlpatterns = [
    
    #path('list_info/', list_info, name='list_info'),
    path('', views.home, name='index'),
    #path('content/', include(router.urls), name='content'),
    path('tinymce/', include('tinymce.urls')),
    path('section', views.SectionList.as_view(), name='section'),
    path('section/<int:pk>/', views.SectionDetail.as_view()),
    path('category', views.CategoryList.as_view(), name='category'),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('content/', views.ContentList.as_view(), name='content'),
    path('content/<int:pk>/', views.ContentDetail.as_view()),
    path('post/', views.PostList.as_view(), name='post'),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('comment/', views.CommentList.as_view(), name='comment'),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),

    path('post_list/', views.post_list, name='post_list'),
    path('post_list/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post_list/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post_list/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('post_list/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    
]
