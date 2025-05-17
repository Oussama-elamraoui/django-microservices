# users/urls.py
from django.urls import path
from .views import UserListView

urlpatterns = [
    path('usersList', UserListView.as_view(), name='user-list'),
]