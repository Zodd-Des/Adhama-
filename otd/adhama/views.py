from django.shortcuts import render
from .models import Job
from .models import Testimony
from .models import Blogs
from .models import LatestPosts
from .models import Training

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
    
    courses = Training.objects.all()

    return render(request, "elements.html", {'courses' : courses})
    
      
def blog(request):


    posts = Blogs.objects.all()
    lposts = LatestPosts.objects.all()

    return render(request, "blog.html", {'posts' : posts , 'lposts' : lposts})
    
    
def contact(request):

    return render(request, "contact.html")
    
    
def privacy(request):

    return render(request, "privacy.html")
    
    
def terms(request):

    return render(request, "terms.html")
    
    
