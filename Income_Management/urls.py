from django.urls import path 
from .views import IncomeSourceView,IncomeView,AddIncomeView

urlpatterns = [
    path('income_categroy/',IncomeSourceView.as_view(),name='income_category'),
    path('incomes/',IncomeView.as_view(),name='income_list'),
    path('income/',AddIncomeView.as_view(),name='add_income'),
]
