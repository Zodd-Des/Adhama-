from django.shortcuts import render
from .models import Job
from .models import Testimony

# Create your views here.

def index(request):

    dests = Job.objects.all()
    destis = Testimony.objects.all()



    return render(request, "index.html",{'dests': dests, 'destis': destis})

def about(request):

    return render(request, "about.html")

    
def offers(request):

    return render(request, "offers.html")
    
       
def elements(request):

    return render(request, "elements.html")
    
    
def blog(request):

    return render(request, "blog.html")
    
    
def contact(request):

    return render(request, "contact.html")
    
    
def privacy(request):

    return render(request, "privacy.html")
    
    
def terms(request):

    return render(request, "terms.html")
    
    
