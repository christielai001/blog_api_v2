from rest_framework import serializers
from .models import CustomUser, Post, Comment, PostLike, CommentLike
from rest_framework.validators import UniqueValidator

# Custom user serializers
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name','username', 'email', 'date_joined']

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

        # extra_kwargs hides the field from the output but allows it in the input 
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    # validation - rules before user can successfully create a new user
    username = serializers.CharField(
        max_length=100, 
        validators = [UniqueValidator(queryset=CustomUser.objects.all())])
        
    email = serializers.EmailField(
        max_length=100, 
        validators = [UniqueValidator(queryset=CustomUser.objects.all())])
        
    password = serializers.CharField(
        min_length=6)
    

    def create(self, validated_data):
        # .pop reads and removes password
        password = validated_data.pop('password')

        # creates user without returning the password
        user = CustomUser.objects.create(**validated_data)

        user.set_password(password)
        user.save()
        return user


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