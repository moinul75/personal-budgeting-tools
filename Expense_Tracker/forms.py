from django import forms
from .models import Expense,Expence_category


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category','amount','description','date']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
        }
        

class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = Expence_category
        fields = ['category_name','budget_goal']
        widgets = {
            'category_name':forms.TextInput(attrs={'class':'form-control'}),
            'budget_goal':forms.TextInput(attrs={'class':'form-control'}),
        }
        
