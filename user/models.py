from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 32,unique=True)
    password = models.CharField(max_length = 36)
    isTermsAccepted = models.BooleanField()