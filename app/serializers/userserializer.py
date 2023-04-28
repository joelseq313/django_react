from rest_framework import serializers
from  app.models import User_Experties

class User_ExpertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Experties
        fields = '__all__'
