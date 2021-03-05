from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api_views import AuthorViewSet, NewsPostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'newsposts', NewsPostViewSet, basename='user')
router.register(r'author', AuthorViewSet)
router.register(r'comment', CommentViewSet)
urlpatterns = [
    path('api/', include(router.urls))
]
urlpatterns += router.urls