from rest_framework import viewsets, permissions
from rest_framework.authentication import BasicAuthentication
from app.models import User_Experties
from app.serializers.userserializer import User_ExpertiesSerializer

class User_Experties_ViewSet(viewsets.ModelViewSet):
    serializer_class = User_ExpertiesSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        if self.request.user.is_superuser:
            return User_Experties.objects.all()
        else:
            return User_Experties.objects.none()

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)
