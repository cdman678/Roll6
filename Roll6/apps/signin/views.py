from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import *
from Roll6.apps.game.logic.game_management import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    form = Login()
    joinform = PartyID()
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect("dashboard/")
            else:
                return render(request, 'signin/signin.html', {'form': form, 'joinform': joinform, 'invalidlogin': True})
        else:
            gamecode = request.POST['id']
            if gamecode is not None:
                if get_game_by_id(gamecode) is not None:
                    return redirect("/game/"+gamecode+"/choosecharacter")
                else:
                    return render(request, 'signin/signin.html', {'form': form, 'joinform': joinform, 'invalidgame': True})
            else:
                return render(request, 'signin/signin.html', {'form': form, 'joinform': joinform, 'invalidgame': True})

    elif request.user.is_authenticated:
        return redirect("dashboard/")
    else:
        return HttpResponse(render(request,'signin/signin.html', {'form': form, 'joinform': joinform}))

@login_required(login_url='index')
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("index")
