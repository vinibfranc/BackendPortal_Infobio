from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from cms.views import SectionViewSet, CategoryViewSet, ContentViewSet
from rest_framework_nested import routers

#from rest_framework_extensions.routers import ExtendedSimpleRouter

router = DefaultRouter()
router.register('section', SectionViewSet, base_name='section')
router.register('category', CategoryViewSet, base_name='category')
router.register('content', ContentViewSet, base_name='content')

'''section_router = routers.NestedSimpleRouter(router, 'section', lookup='section')
section_router.register('category', CategoryViewSet, base_name='category')

category_router = routers.NestedSimpleRouter(section_router, 'category', lookup='category')
category_router.register('content', ContentViewSet, base_name='content')

content_router = routers.NestedSimpleRouter(category_router, 'content', lookup='content')
#content_router.register('content', ContentViewSet, base_name='content')'''


'''router = ExtendedSimpleRouter()
(
    router.register(r'section', SectionViewSet, base_name='section')
          .register(r'category',
                    CategoryViewSet,
                    base_name='section-category',
                    parents_query_lookups=['section_category'])
          .register(r'content',
                    ContentViewSet,
                    base_name='section-category-content',
                    parents_query_lookups=['category__section', 'category'])
)
#urlpatterns = router.urls'''


'''class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
   pass

router = NestedDefaultRouter()

section_router = router.register('section', SectionViewSet)

section_router.register(
    'category', CategoryViewSet,
    base_name='section-category',
    parents_query_lookups=['section']
    ).register('content',
           ContentViewSet,
           base_name='section-category-content',
           parents_query_lookups=['category__section', 'category'])'''

