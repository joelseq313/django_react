from rest_framework import generics,viewsets
from app.serializers.signupserializer import SignupSerializer
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, status

from rest_framework import viewsets, permissions

from rest_framework import viewsets, permissions
class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to access list views and
    authenticated users to create new users.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # Allow read-only access to everyone.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_superuser

class SignUpViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = SignupSerializer
   
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            # If the user is not a superuser, return an empty queryset
            return User.objects.none()

    

    
   
   
  

   
    
