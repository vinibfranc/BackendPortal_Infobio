from django.urls import include, path
#from cms.api import router
from . import views
from cms.views import OpportunityView

urlpatterns = [
    
    path('', views.home, name='index'),
    #path('content/', include(router.urls), name='content'),
    path('tinymce/', include('tinymce.urls')),


    path('principal', views.HomepageList.as_view(), name='principal'),
    path('principal/<int:pk>/', views.HomepageDetail.as_view(), name='homepage'),
    path('sobre', views.AboutList.as_view(), name='sobre'),
    path('sobre/<int:pk>/', views.AboutDetail.as_view()),
    path('grande-area', views.AreaBigCategoryList.as_view(), name='grande-area'),
    path('grande-area/<int:pk>/', views.AreaBigCategoryDetail.as_view()),
    path('area-especifica', views.SpecificAreaList.as_view(), name='area-especifica'),
    path('area-especifica/<int:pk>', views.SpecificAreaDetail.as_view()),
    path('oportunidades', views.OpportunityList.as_view(), name='oportunidades'),
    path('oportunidades/<int:pk>', views.OpportunityDetail.as_view()),

    path('adicionar-oportunidade', OpportunityView.as_view(), name='adicionar-oportunidade'),
]
