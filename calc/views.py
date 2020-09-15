from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'xxx'})

def add(request):

    investment = int(request.POST['investment'])
    year = int(request.POST['year'])
    r = float(request.POST['r'])
    i = float(request.POST['i'])

    r = r/100 + 1
    f = investment * (pow(r,year) -1)
    f = f / (r-1)
    res = investment + r*f

    return render(request, 'results.html', {'result' : res})