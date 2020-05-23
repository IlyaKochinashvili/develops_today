from django.db.models import F
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, pk, ):
        post = Post.objects.get(pk=pk)
        post.amount_of_upvotes = F('amount_of_upvotes') + 1
        post.save()
        return Response({}, status=200)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
