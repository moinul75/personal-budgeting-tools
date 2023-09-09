from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomUserManager

# Create your models here.
#email,username,profile_photo,Address 
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=150,unique=True)
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    last_name = models.CharField(max_length=150,blank=True)
    address = models.CharField(max_length=250,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profile/',null=True,blank=True) 
    
    
    #required fields 
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']
    
    def __str__(self) -> str:
        return self.email 
    
    
    
