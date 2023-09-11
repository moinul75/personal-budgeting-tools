from django import forms
from . models import Income_Source,Income


class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = Income_Source
        fields = ['source_name','income_goal']
        widgets = {
            'source_name':forms.TextInput(attrs={'class':'form-control'}),
            'income_goal':forms.TextInput(attrs={'class':'form-control'})
        }
        

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source','amount','description','date']
        widgets = {
            'source':forms.Select(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-contol'}),
            'date':forms.DateInput(attrs={'type':'date','class':'form-control'})
        }