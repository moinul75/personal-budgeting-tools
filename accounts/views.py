from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email,password=password)
        print(user)
        if user is None:
            messages.error(request,f"user is not found..email or password are not found")
            return redirect('login')
        else:
            login(request,user)
            messages.success(request, f'{user} is logged is successfullly')
            return redirect('expense_list')    
    else:
        pass 
    return render(request,'login.html')

#logout
@login_required
def Logout(request):
    logout(request)
    return redirect('login')

  


