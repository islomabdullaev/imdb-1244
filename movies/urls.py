from django.urls import path
from movies.views import movie_list

urlpatterns = [
    path('list/', movie_list)
]