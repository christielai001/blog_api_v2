from rest_framework import serializers
from .models import CustomUser, Post, Comment, PostLike, CommentLike

# Custom user serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name','username', 'email', 'date_joined']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['author', 'date_posted']
        fields = ['id', 'author','title', 'content', 'date_posted']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        read_only_fields = ['author', 'date_posted']
        fields = ['id', 'author','post', 'content', 'date_posted']

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        read_only_fields = ['author']
        fields = ['id', 'author','post']

class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        read_only_fields = ['author']
        fields = ['id', 'author','comment']