from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='index')
def maindash(request):
    temp =get_template('dashboard/maindash.html')
    return HttpResponse(temp.render())

@login_required(login_url='index')
def motwfaq(request):
    temp = get_template('dashboard/motwfaq.html')
    return HttpResponse(temp.render())

@login_required(login_url='index')
def roll6faq(request):
    temp = get_template('dashboard/roll6faq.html')
    return HttpResponse(temp.render())

def wifu(request):
    temp = get_template('dashboard/wifu.html')
    return HttpResponse(temp.render())
