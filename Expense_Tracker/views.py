from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import  ListView
from .forms import ExpenseForm,ExpenseCategoryForm
from .models import Expense,Expence_category
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required
class AddExpenseView(LoginRequiredMixin,View):
    template_name = 'add_expense.html'
    form_class = ExpenseForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
        return render(request, self.template_name, {'form': form})
    

class ExpenseListView(LoginRequiredMixin,ListView):
    template_name = 'expense_list.html'

    def get(self, request):
        expenses = Expense.objects.filter(user=request.user)
        return render(request, self.template_name, {'expenses': expenses})

  
class ExpenseCategory(LoginRequiredMixin,View):
    template_name = 'expense_category.html'
    form_class = ExpenseCategoryForm
    
    #show the form 
    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})
    
    #post the form 
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            expense_cat = form.save(commit=False)
            expense_cat.user = request.user
            expense_cat.save()
            return redirect('expense_category')
        return render(request,self.template_name,{'form':form})
    
#make this expense visulation 

    
    
    
