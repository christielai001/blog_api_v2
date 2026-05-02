from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomUserSerializer, PostSerializer, CommentSerializer
from .models import CustomUser, Post, Comment, PostLike, CommentLike
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # only authenticated user can perform any request if not other user are just able to view the content
    permission_classes = [IsAuthenticated]
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # set logged-in user as the author of the post
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = request.user

        # define existing likes
        existing_like = PostLike.objects.filter(
            user=user, 
            post_id=pk
        ).first()

        # created conditions: if user has a like we delete it which is unliking post 
        #                     if user does not have a like on post we create a like
        if existing_like:
            existing_like.delete()
            return Response({"liked":False})

        else:
            PostLike.objects.create(
                user=user, 
                post_id=pk
            )
            return Response({"liked":True}, status=200)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # only gives comments to specific post so it does not return all comments in the database
    def get_queryset(self):
        post_id = self.request.query_params.get('post')

        if post_id:
           return Comment.objects.filter(post_id=post_id)

        return Comment.objects.all()

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        user = request.user

        existing_like = CommentLike.objects.filter(
            user=user, 
            comment_id=pk
        ).first()

        if existing_like:
            existing_like.delete()
            return Response({"liked":False})

        else:
            CommentLike.objects.create(
                user=user, 
                comment_id=pk
            )
            return Response({"liked":True}, status=200)


