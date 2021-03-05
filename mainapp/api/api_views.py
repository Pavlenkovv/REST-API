from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import AuthorSerializer, CommentSerializer, NewsPostSerializer
from ..models import Author, NewsPost, Comment


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class NewsPostViewSet(viewsets.ModelViewSet):
    serializer_class = NewsPostSerializer
    queryset = NewsPost.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.amount_of_upvotes += 1
        post.save()
        return Response({'status': 'post upvoted'})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
