from rest_framework import generics

from user.serializers import UserSerialier


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerialier
