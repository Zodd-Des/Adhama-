from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('offers.html', views.offers, name='offers'),
    path('elements.html', views.elements, name='elements'),
    path('blog.html', views.blog, name='blog'),
    path('contact.html', views.contact, name='contact'),
    path('privacy.html', views.privacy, name='privacy'),
    path('terms.html', views.terms, name='terms')
    ]