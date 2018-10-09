from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from cms.views import SectionViewSet, CategoryViewSet, ContentViewSet

router = DefaultRouter()
router.register('section', SectionViewSet, base_name='section')
router.register('category', CategoryViewSet, base_name='category')
router.register('content', ContentViewSet, base_name='content')

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

section_router = router.register('section', SectionViewSet)
section_router.register(
    'category', CategoryViewSet,
    base_name='section-category',
    parents_query_lookups=['section']
    )

'''section_router.register(
    'category', CategoryViewSet,
    base_name='section-category',
    parents_query_lookups=['section']
    ).register('content',
           ContentViewSet,
           base_name='section-category-content',
           parents_query_lookups=['category__section', 'category']
        )'''

