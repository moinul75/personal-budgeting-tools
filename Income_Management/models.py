from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.
class Income_Source(models.Model):
    source_name = models.CharField(max_length=250,blank=True)
    income_goal = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.source_name
    

class Income(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    source = models.ForeignKey(Income_Source,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    date = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    #source,amount,description 
    
    def __str__(self) -> str:
        return f"{self.user.username} - {self.source}"
    
    
