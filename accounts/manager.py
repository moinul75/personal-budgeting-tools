from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username,password,**extra_fields):
        if not username:
            raise ValueError("Username must be set")
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(
           username=username,
           email=email,
          **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,password,username,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be is_staff True")
        if extra_fields.get('is_active') is not True:
            raise ValueError("Superuser must be is_active True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser True')
        
        return self.create_user(email, username, password, **extra_fields)
       
    