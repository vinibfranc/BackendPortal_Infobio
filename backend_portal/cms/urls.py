from django.urls import include, path
#from cms.api import router
from . import views

urlpatterns = [
    
    path('', views.home, name='index'),
    #path('content/', include(router.urls), name='content'),
    path('tinymce/', include('tinymce.urls')),

    #path('post_list/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #path('post_list/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    #path('post_list/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('homepage', views.HomepageList.as_view(), name='homepage'),
    path('homepage/<int:pk>/', views.HomepageDetail.as_view(), name='homepage'),
    path('about', views.AboutList.as_view(), name='about'),
    path('about/<int:pk>/', views.AboutDetail.as_view()),
    path('big-area', views.AreaBigCategoryList.as_view(), name='big-area'),
    path('big-area/<int:pk>/', views.AreaBigCategoryDetail.as_view()),
    path('specific-area', views.SpecificAreaList.as_view(), name='specific-area'),
    path('specific-area/<int:pk>', views.SpecificAreaDetail.as_view()),
    path('opportunities', views.OpportunityList.as_view(), name='opportunities'),
    path('opportunities/<int:pk>', views.OpportunityDetail.as_view())
]
