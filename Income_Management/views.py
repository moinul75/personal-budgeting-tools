from django.shortcuts import render,redirect
from .models import Income,Income_Source
from .forms import IncomeForm,IncomeSourceForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.views.generic import  ListView

# adding income 
class IncomeSourceView(LoginRequiredMixin,View):
    template_name = 'income_categroy.html'
    form_class = IncomeSourceForm
    
    #get the from 
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})
    
    #post the from 
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Created Income Categroy Successfully')
            return redirect('income_category')
        return render(request,self.template_name,{'form':form})
    


#now view the income list 
class IncomeView(LoginRequiredMixin,ListView):
    template_name = 'income_list.html'
    
    def get(self,request):
        incomes = Income.objects.filter(user=request.user)
        return render(request, self.template_name,{'incomes':incomes})
        

    

    
    




#adding income view 
class AddIncomeView(LoginRequiredMixin, View):
    template_name = 'add_income.html'
    form_class = IncomeForm
    
    #now open the form 
    def get(self,request):
        #get the form 
        form = self.form_class
        return render(request, self.template_name, {'form':form})
    
    #now crete form 
    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, f'Income added to the list successfully...')
            return redirect('income_list')
        return render(request,self.template_name, {'form':form})
    
        

