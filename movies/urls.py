from django.urls import path
from movies.views import MovieListAPIView, StreamPlatformListAPIView, MovieReviewCreateAPIView

urlpatterns = [
    path('list', MovieListAPIView.as_view()),
    path('create_review', MovieReviewCreateAPIView.as_view()),
    path('streams/list', StreamPlatformListAPIView.as_view()),
]