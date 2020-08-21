from django.shortcuts import render
from .models import Job
from .models import Testimony

# Create your views here.

def index(request):

    dests = Job.objects.all()
    destis = Testimony.objects.all()



    return render(request, "index.html",{'dests': dests, 'destis': destis})
    
