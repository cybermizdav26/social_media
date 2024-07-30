from rest_framework import parsers
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.post.api.version0.permissions import IsOwner
from apps.post.api.version0.serializers import (
    PostCreateSerializer,
    PostUpdateSerializer,
    PostListSerializer,
    CommentCreateSerializer, CommentListSerializer, PostDeleteSerializer, CommentDeleteSerializer,
)
from apps.post.models import Post, LikedPost, Comment


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostCreateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    # parser_classes = (parsers.MultiPartParser, parsers.FileUploadParser, parsers.JSONParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


post_create = PostCreateAPIView.as_view()


class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    permission_classes = [IsOwner]

    lookup_field = 'id'

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj


post_update = PostUpdateAPIView.as_view()


class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


post_list = PostListAPIView.as_view()


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'


post_delete = PostDeleteAPIView.as_view()


class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('id')
        post = Post.objects.get(id=post_id)
        like = LikedPost.objects.filter(post=post, user=request.user).first()

        if not like:
            LikedPost.objects.create(user=request.user, post=post)
            return Response({"message": "liked"})
        return Response({"message": "disliked"})


like_post = LikePostAPIView.as_view()


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



comment_create = CommentCreateAPIView.as_view()


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    queryset = Comment.objects.all()


comment_list = CommentListAPIView.as_view()


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'


comment_delete = PostDeleteAPIView.as_view()
