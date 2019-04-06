from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render
from .form import Login
from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return render(request,'signin/signin.html')


    else:
        form = Login()
        t = get_template('signin/signin.html')
        return HttpResponse(render(request,'signin/signin.html', {'form': form}))
