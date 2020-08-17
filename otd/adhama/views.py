from django.shortcuts import render
from .models import Job
from .models import Testimony

# Create your views here.

def index(request):

    dest1 = Job()
    dest1.name = 'Social Media Manager'
    dest1.desc = 'Social Media Managers are in sharge of representing a company across all social channels as the voice of the brand. They respond to comments ,complile campaigns amd create content.Social media managers create and maintain brand...'
    dest1.img = 'socialmedia.jpg'

    dest2 = Job()
    dest2.name = 'Content Creator'
    dest2.desc = 'A content creator is someone who is responsible for the contribution of information to any media and most especially to digital media. They usually target a specific audience in specific contexts.A content creator produces entertaining'
    dest2.img = 'graphics2.jpg'

    dest3 = Job()
    dest3.name = 'Digital Media Manager'
    dest3.desc = 'Digital media managers oversee the development, production, and review of site content,videos and blog posts. These individuals have the experience to oversee digital media efforts of a company, including websites...'
    dest3.img = 'graphics.jpg'

    dest4 = Job()
    dest4.name = 'Transcriptionist'
    dest4.desc = 'A person who does the transcription is known as a transcriptionist or transcriber. Transcription is a challenging and specialist function requiring specific skill sets and the ability to multitask. ... Fast and accurate typing skills...'
    dest4.img = 'digital.jpeg'

    dests = [dest1, dest2, dest3, dest4]

    
    
    desti1 = Testimony()
    desti1.name = 'Christopher Multisanti'
    desti1.name2 = 'Programmer'
    desti1.desc = 'Whether you want to learn new skills, make more money, or find a job, we’ll send you emails each week with a clear game plan'
    desti1.img = '1.png'

    desti2 = Testimony()
    desti2.name = 'Ritchie April'
    desti2.name2 = 'Social Media Manager'
    desti2.desc = 'Every day, our career experts help real women reach their goals. Now we will deliver their advice straight to your inbox.'
    desti2.img = 'immg2.jpg'

    desti3 = Testimony()
    desti3.name = 'Donna Gabbana'
    desti3.name2 = 'Content Creator'
    desti3.desc = 'A content creator is someone who is responsible for the contribution of information to any media and most especially to digital media.'
    desti3.img = 'pic4.jpg'

    desti4 = Testimony()
    desti4.name = 'Carmine Lupatasi'
    desti4.name2 = 'Marketing Manager'
    desti4.desc = 'I have become thoroughly addicted to the newsletter and online resources,"I read about a career in events..'
    desti4.img = 'pic8.jpg'

    desti5 = Testimony()
    desti5.name = 'Billy kimber'
    desti5.name2 = 'Fullstack developer'
    desti5.desc = 'We’re also including downloadable worksheets, quizzes, and guides, custom-designed and tailored to each track'
    desti5.img = 'immg5.jpg'

    destis = [desti1, desti2, desti3, desti4, desti5]


    return render(request, "index.html",{'dests': dests, 'destis': destis})
    
