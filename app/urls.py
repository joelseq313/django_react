
from django.urls import path,include
from  . viewsets.singupviewset import  SignUpViewSet
from . viewsets.signinviewset import SignInViewSet
from .viewsets.userexperties import User_Experties_ViewSet
from .viewsets.logoutview import LogoutAPIView

from rest_framework import routers
from django.urls import path
from django.urls import path
from rest_framework import routers



router = routers.DefaultRouter()
router.register('sigup',SignUpViewSet, basename='signup')
router.register('user_experties',User_Experties_ViewSet,basename='user_experties')




urlpatterns = [
  
    path('', include(router.urls)),
     path('login/', SignInViewSet.as_view(), name='login'),
     path('logout/',LogoutAPIView.as_view(), name='logout'),
    


]