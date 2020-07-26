from django.shortcuts import render

# Create your views here.

def nickel(requests):
    return render(requests, 'welcome.html')
