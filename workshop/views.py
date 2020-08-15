from django.shortcuts import render
from .models import Arttherapy, Publication, updates, Gallery

# Create your views here.

def index(request):

    dests = Arttherapy.objects.all()
    pub = Publication.objects.all()
    upda = updates.objects.all()
    

    return render(request, "index.html", {'dests' : dests, 'pub': pub, 'upda': upda})

def gallery(request):

    gal = Gallery.objects.all()

    return render(request,"gallery.html", {'gal': gal})

def about(request):
    upda = updates.objects.all()

    return render(request,"about.html", {'upda': upda})