from django.shortcuts import render

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['Si vols contactar amb mi, sisplau enviam un email','fbassas@gmail.com']})
