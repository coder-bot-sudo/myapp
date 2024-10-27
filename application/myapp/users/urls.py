# user/urls.py
from django.urls import path
from .views import UserListView, UserCreateView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
]