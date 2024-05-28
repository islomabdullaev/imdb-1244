from django.urls import path
from movies.views import MovieListAPIView, StreamPlatformListAPIView

urlpatterns = [
    path('movies/list', MovieListAPIView.as_view()),
    path('streams/list', StreamPlatformListAPIView.as_view())
]