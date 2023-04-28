
from django.db import models
from django.contrib.auth.models import User

class User_Experties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experties=models.CharField(max_length=100,blank=False)
   


