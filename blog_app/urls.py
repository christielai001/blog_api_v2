from django.urls import path
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = router.urls