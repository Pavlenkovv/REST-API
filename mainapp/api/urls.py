from rest_framework.routers import DefaultRouter

from .api_views import AuthorListAPISet, NewsPostViewSet, CommentListAPISet


router = DefaultRouter()
router.register(r'newsposts', NewsPostViewSet, basename='user')
urlpatterns = router.urls
