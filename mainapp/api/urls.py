from django.urls import path

from .api_views import AuthorListAPIView, NewsPostListAPIView, CommentListAPIView


urlpatterns = [
    path('authors/', AuthorListAPIView.as_view()),
    path('comments/', CommentListAPIView.as_view()),
    path('newspost/', NewsPostListAPIView.as_view()),
    path('newspost/<int:pk>', NewsPostListAPIView.as_view()),
]
