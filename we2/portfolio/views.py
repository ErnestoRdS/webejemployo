from django.shortcuts import render
from .models import Portfolio 

def portfolio(request): 
    projects = Portfolio.objects.all()

    return render(request, 'portfolio/portfolio.html', {'projects':projects})
