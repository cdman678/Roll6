from django.template.loader import get_template
from django.http import HttpResponse
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


