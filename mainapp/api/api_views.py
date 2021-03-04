from rest_framework import viewsets

from .serializers import AuthorSerializer, CommentSerializer, NewsPostSerializer
from ..models import Author, NewsPost, Comment


class AuthorListAPISet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class NewsPostViewSet(viewsets.ModelViewSet):
    serializer_class = NewsPostSerializer
    queryset = NewsPost.objects.all()


class CommentListAPISet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
