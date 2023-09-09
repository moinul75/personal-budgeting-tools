from django.urls import path 
from .views import Login,Logout,Signup

urlpatterns = [
    path('',Login,name='login'),
    path('signup/',Signup,name='signup'),
    path('logout/',Logout,name='logout'),
]
