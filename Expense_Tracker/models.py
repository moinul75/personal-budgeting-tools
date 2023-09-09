from django.db import models
from accounts.models import User

# Create your models here.
#model: Expence Categroy and expence 
class Expence_category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category_name = models.CharField(max_length=150)
    budget_goal = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def total_expense(self):
        total = 0
        expenses = Expense.objects.filter(category=self)
        for expense in expenses:
            total += expense.amount
        return total
    
    def __str__(self):
        return self.category_name
    

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Expence_category,on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.category}"
    
    

    
    
