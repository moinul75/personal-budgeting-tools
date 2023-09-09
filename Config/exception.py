from django.shortcuts import render




#handle 404 errors page 
def handler404(request,*args, **argsv):
    response = render(request, '404.html')
    response.status_code = 404 
    return response