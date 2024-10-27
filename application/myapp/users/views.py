# users/views.py
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Listet alle Benutzer auf
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Erstellt einen neuen Benutzer
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer