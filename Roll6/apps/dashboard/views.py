from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.

def maindash(request):
    temp =get_template('dashboard/maindash.html')
    return HttpResponse(temp.render())

def motwfaq(request):
    temp = get_template('dashboard/motwfaq.html')
    return HttpResponse(temp.render())

def roll6faq(request):
    temp = get_template('dashboard/roll6faq.html')
    return HttpResponse(temp.render())

def wifu(request):
    temp = get_template('dashboard/wifu.html')
    return HttpResponse(temp.render())
