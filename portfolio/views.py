from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from portfolio import models
from portfolio.models import Contact

def landing_page(request):
    return render(request, 'landing.html')

def about_page(request):
    return render(request, 'about.html')

def skills_page(request):
    return render(request, 'skills.html')

def projects_page(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method== "POST":
        print('post')
        name= request.POST.get('name')
        email= request.POST.get('email')
        number= request.POST.get('number')
        message= request.POST.get('message')
        print(name, email, number, message)

        if len(name)>1 and len(name)<30:
            pass
        else:
            messages.errors(request, 'Length of name should be greater than 2 and less than 30 characters')
            return render(request, 'home.html')
        
        if len(email)>1 and len(email)<30:
            pass
        else:
            messages.error(request, 'Invalid email')
            return render(request, 'home.html')
        
        if len(number)>2 and len(number)<13:
            pass
        else:
            messages.error(request, 'invalid number')
            return render(request, 'home.html')
        
        ins= models.Contact(name=name, email=email, number=number, message=message)
        ins.save()
        messages.success(request, 'Thank you for contacting me! Your message has been sent.')
        print('success')
    return render(request, 'home.html')