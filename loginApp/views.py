from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login
from django.http import HttpResponse

from .forms import LoginForm
from user.models import User
# from project.views import show_user

# Create your views here.
def show_login_form(request):
    form = LoginForm()
    if(request.method == "POST"):
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = request.POST.get('username')
            password = request.POST.get('password')
            context = {
                'form':form,
                'errors':[],
            }
            if(not(User.objects.filter(username = username).exists())):
                context.get('errors').append('Enter a valid username !')
            if(len(context.get('errors')) == 0 and not(password == User.objects.get(username = username).password)):
                context.get('errors').append('The password is incorrect !')

            if(len(context.get('errors')) == 0):
                url = f'home/{username}'
                return redirect('/' + url + '/')

            return render(request,'login/loginForm.html',context)

    context = {
        'form':form,
    }
    return render(request,'login/loginForm.html',context)