from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect

from user.models import User
from .forms import SignupForm

# Create your views here.
def show_signup_form(request):
    form = SignupForm()

    if(request.method == "POST"):
        form = SignupForm(request.POST)
        if(form.is_valid()):
            username = request.POST.get('username')
            password = request.POST.get('password')
            context = {
                'form':form,
                'errors':[]
            }
            if(User.objects.filter(username = username).exists()):
                context.get('errors').append(f'Username {username} is already taken')
                return render(request,'signup/signupForm.html',context)
            else:
                isTermsAccepted = request.POST.get('isTermsAccepted')

                if(isTermsAccepted is not None):
                    isTermsAccepted = True
                else:
                    isTermsAccepted  = False

                User.objects.create(username = username,password = password,isTermsAccepted = isTermsAccepted)
                url = f"home/{username}"

                return redirect('/' + url + '/')
                # return redirect(f'home/{username}/') it wont redirect properly

    context = {
        'form':form
    }
    return render(request,'signup/signupForm.html',context)