from django.urls import path 
from .views import Login,Logout

urlpatterns = [
    path('',Login,name='login'),
    path('logout/',Logout,name='logout'),
]
