from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    # stores all albums in database into all_albums
    all_albums = Album.objects.all()
    # django already set up to look into a template dir (if u create or it exists)
    template = loader.get_template("music/index.html")
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))



def detail(request, album_id):
    return HttpResponse("<h2>details for album_id: " + str(album_id) +"</h2>")
