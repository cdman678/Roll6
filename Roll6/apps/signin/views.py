from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import Login
from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
    form = Login()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect("dashboard/")
        else:
            return render(request, 'signin/signin.html', {'form': form, 'invalid': True})

    else:
        return HttpResponse(render(request,'signin/signin.html', {'form': form}))
