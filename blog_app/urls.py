from django.urls import path, include
from .views import PostViewSet, CommentViewSet, RegistrationAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('post', PostViewSet, basename='post')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegistrationAPIView.as_view()),
    
]
