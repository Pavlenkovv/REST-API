from rest_framework.response import Response
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView
from .serializers import AuthorSerializer, CommentSerializer, NewsPostSerializer
from ..models import Author, NewsPost, Comment


class AuthorListAPIView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class NewsPostListAPIView(APIView):
    # serializer_class = NewsPostSerializer
    # queryset = NewsPost.objects.all()

    def get(self, request):
        newsposts = NewsPost.objects.all()
        serializer = NewsPostSerializer(newsposts, many=True)
        return Response({'newsposts': serializer.data})

    def post(self, request):
        newsposts = request.data.get('newsposts')
        serializer = NewsPostSerializer(data=newsposts)
        if serializer.is_valid(raise_exception=True):
            newspost_saved = serializer.save()
        return Response({f"success": "News post'{newspost_saved.title}' created successfully"})

    def put(self, request, pk):
        saved_newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
        data = request.data.get('newspost')
        serializer = NewsPostSerializer(instance=saved_newspost, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            newspost_saved = serializer.save()
        return Response({f"success": "News post'{newspost_saved.title}' updated successfully"})

    def delete(self, request, pk):
        newspost = get_object_or_404(NewsPost.objects.all(), pk=pk)
        newspost.delete()
        return Response({"message": f'News post with id `{pk}` has been deleted.'}, status=204)


class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
