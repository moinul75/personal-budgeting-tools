from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form  = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # print(form.cleaned_data)
            messages.success(request,f'User is Signup Successfully ')
            return redirect('login')
    if request.user.is_authenticated: 
        messages.warning(request,f"You are already logged in")
        return redirect('expense_list')
    else: 
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request,'signup.html',context)




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



#password reset 



#forget password email validation 



  


