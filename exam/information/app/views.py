from django.shortcuts import render , redirect
from .models import *
# Create your views here.

def home(request):
    employee = Employee.objects.all()[:4]
    data = {
        'employee' : employee,
    }
    return render(request, 'index.html', context=data)

def employee(request):
    employee =  Employee.objects.all()
    data = {
        'employee' : employee,
    }
    return render(request, 'employee.html', context=data)

def news(request):
    news = News.objects.all().order_by('-id')
    data = {
        'news' : news,
    }
    return render(request, 'news.html', context=data)

def contact(reuqest):
    if reuqest.method == 'POST':
        name = reuqest.POST.get('name')
        email = reuqest.POST.get('email')
        message = reuqest.POST.get('message')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return redirect('/')