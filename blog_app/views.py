from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer, PostSerializer, CommentSerializer, PostLikeSerializer, CommentLikeSerializer
from .models import CustomUser, Post, Comment, PostLike, CommentLike
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # only authenticated user can perform any request if not other user are just able to view the content
    permission_classes = IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsAuthenticatedOrReadOnly

    # set logged-in user as the author of the post
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = IsAuthenticatedOrReadOnly

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    permission_classes = IsAuthenticatedOrReadOnly

    # user instead of author
        # - not creating or providing content to anything just an action to the object
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class CommentLikeViewSet(viewsets.ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    permission_classes = IsAuthenticatedOrReadOnly

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
