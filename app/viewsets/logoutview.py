from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import logout
from rest_framework.authentication import BasicAuthentication
class LogoutAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        response_data = {
            'message': 'You have been logged out successfully.',
            'status': 'success'
        }
        return Response(response_data)
