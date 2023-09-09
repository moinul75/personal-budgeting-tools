from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import  ListView
from .forms import ExpenseForm,ExpenseCategoryForm
from .models import Expense,Expence_category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum,Min, Max,F
from django.db.models.functions import TruncMonth  # Import TruncMonth to group by month
from datetime import datetime




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
    
# def expense_stats(request):
#     expense_cat = Expence_category.objects.all()

#     # # Define default date range (e.g., this month)
#     # start_date = datetime.now().replace(day=1)
#     # end_date = datetime.now()

#     # Get the selected date range option from the query parameters
#     date_range_option = request.GET.get('date_range_option', 'this_month')

#     if date_range_option == 'this_month':
#         start_date = datetime.now().replace(day=1)
#         end_date = datetime.now()
#     elif date_range_option == 'monthly_wise':
#     # You can implement logic to select a custom date range for "monthly_wise" here
#         start_date = request.GET.get('start_date')
#         end_date = request.GET.get('end_date')
#         print(start_date, end_date)
#         if start_date and end_date:
#             start_date = datetime.strptime(start_date, '%Y-%m-%d')
#             end_date = datetime.strptime(end_date, '%Y-%m-%d')
#             print(start_date, end_date)
#         else:
#             # Handle the case where start_date or end_date is not provided or invalid
#             # You can set default values or raise an error as needed
#             start_date = datetime.now().replace(day=1)
#             end_date = datetime.now()
            
#             # Corrected query for monthly-wise
#             monthly_stats = Expense.objects.annotate(
#                 month=TruncMonth('date')
#             ).filter(date__range=[start_date, end_date]).values('month').annotate(
#                 total_budget=Sum(F('category__budget_goal')),
#                 total_expenses=Sum('amount')
#             )

#             # Get the full URL
#             full_url = request.build_absolute_uri()

#             print("Full URL:", full_url)

#     elif date_range_option == 'total_wise':
#         # You can implement logic to select a custom date range for "total_wise" here
#         # For example, you can parse start_date and end_date from query parameters
#         pass

#     # Calculate total expenses for each category within the selected date range
#     for cat in expense_cat:
#         cat.total_expenses = Expense.objects.filter(category=cat, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
#         cat.highest_expense = Expense.objects.filter(category=cat).aggregate(Max('amount'))['amount__max'] or 0
#         cat.lowest_expense = Expense.objects.filter(category=cat).aggregate(Min('amount'))['amount__min'] or 0
#         cat.budget_status = cat.budget_goal - cat.total_expenses

#     # Calculate overall total budget and expenses for each month (if needed)
#     monthly_stats = []
#     if date_range_option == 'monthly_wise':
#         monthly_stats = Expense.objects.annotate(
#             month=TruncMonth('date')
#         ).filter(expense_date__range=[start_date, end_date]).values('month').annotate(
#             total_budget=Sum(F('category__budget_goal')),
#             total_expenses=Sum('amount')
#         )

#     context = {
#         'expense_cat': expense_cat,
#         'monthly_stats': monthly_stats,
#         'date_range_option': date_range_option,  # Pass the selected option to the template
#     }
#     return render(request, 'expense_stats.html', context)

    
def expense_stats(request):
    expense_cat = Expence_category.objects.all()
    date_range_option = request.GET.get('date_range_option', 'this_month')

    if date_range_option == 'this_month':
        start_date = datetime.now().replace(day=1)
        end_date = datetime.now()
    elif date_range_option == 'monthly_wise':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        else:
            start_date = datetime.now().replace(day=1)
            end_date = datetime.now()
    elif date_range_option == 'total_wise':
        # You can implement logic to select a custom date range for "total_wise" here
        # For example, you can parse start_date and end_date from query parameters
        pass

    monthly_stats = []  # Initialize it here

    if date_range_option == 'monthly_wise':
        monthly_stats = Expense.objects.annotate(
            month=TruncMonth('date')
        ).filter(date__range=[start_date, end_date]).values('month').annotate(
            total_budget=Sum('category__budget_goal'),
            total_expenses=Sum('amount')
        )

    for cat in expense_cat:
        cat.total_expenses = Expense.objects.filter(category=cat, date__range=[start_date, end_date]).aggregate(Sum('amount'))['amount__sum'] or 0
        cat.highest_expense = Expense.objects.filter(category=cat).aggregate(Max('amount'))['amount__max'] or 0
        cat.lowest_expense = Expense.objects.filter(category=cat).aggregate(Min('amount'))['amount__min'] or 0
        cat.budget_status = cat.budget_goal - cat.total_expenses

    context = {
        'expense_cat': expense_cat,
        'monthly_stats': monthly_stats,
        'date_range_option': date_range_option,
    }
    return render(request, 'expense_stats.html', context)
    
    
