from django.urls import path 
from Expense_Tracker.views import ExpenseListView,AddExpenseView,ExpenseCategory,expense_stats


urlpatterns = [
    path('expense_list',ExpenseListView.as_view(),name='expense_list'),
    path('add_expense',AddExpenseView.as_view(),name='add_expense'),
    path('expense_category',ExpenseCategory.as_view(),name='expense_category'),
    path('expense_stats',expense_stats,name='expense_stats')
]
