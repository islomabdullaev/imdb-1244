from django.urls import path

from users.views import UserListAPIView

urlpatterns = [
    path('list/', UserListAPIView.as_view())
]