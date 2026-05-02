from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# django has built in custom user: AbstractUser
#   - it handles everything from username, email, password, date_joined, etc
class CustomUser(AbstractUser):
    pass

# Post feature
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.author}' '{self.title}' '{self.date_posted}'"

# Comment feature
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"'{self.author}' '{self.date_posted}'"

# Likes feature for Post
class PostLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # User can only like a post once
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_PostLike")
        ]

    def __str__(self):
        return f"PostLike {self.id}: {self.user} by {self.post}"
    
# Likes feature for Comment
class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    # User can only like a comment once
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "comment"], name="unique_CommentLike")
        ]

    def __str__(self):
        return f"CommentLike {self.id}: {self.user} by {self.comment}"